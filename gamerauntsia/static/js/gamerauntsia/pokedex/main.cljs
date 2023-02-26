(ns main
  (:require [clojure.string :as str]
            [re-frame.core :as rf]
            [reagent.core :as r]
            [reagent.dom :as rdom]))

(rf/reg-fx
 ::make-request
 (fn [{:keys [uri on-success-evt on-failure-evt]}]
   (-> (js/fetch uri)
       (.then
        (fn [response]
          (if (.-ok response)
            (if (str/starts-with?
                 (.get (.-headers response) "Content-Type")
                 "application/json")
              (-> (.json response)
                  (.then
                   (fn [obj]
                     (let [m (js->clj obj :keywordize-keys true)]
                       (rf/dispatch (conj on-success-evt m))))))
              (rf/dispatch (conj on-success-evt (.-body response))))
            (rf/dispatch (conj on-failure-evt))))))))

(rf/reg-fx
 ::set-history
 (fn [{:keys [query-params]}]
   (let [url (js/URL. js/window.location)]
     (doseq [[k _] (.entries (.-searchParams url))]
       (.delete (.-searchParams url) k))
     (doseq [[k v] query-params]
       (.set (.-searchParams url) k v))
     (.pushState js/window.history #js {} "" url))))

(rf/reg-sub
 ::selected-pokemon
 (fn [db _]
   (get db :selected-pokemon)))

(rf/reg-event-db
 ::set-selected-pokemon
 (fn [db [_ pokemon-id]]
   (assoc db :selected-pokemon pokemon-id)))

(rf/reg-sub
 ::pokedex
 (fn [db _]
   (get db :pokedex)))

(rf/reg-sub
 ::pokedex-entry
 (fn [db [_ id]]
   (some #(when (= (:id %) id) %)
         (get db :pokedex))))

(rf/reg-event-db
 ::set-pokedex
 (fn [db [_ pokedex]]
   (assoc db :pokedex pokedex)))

(rf/reg-event-fx
 ::got-pokedex
 (fn [_ [_ response]]
   {:fx [[:dispatch [::set-pokedex response]]]}))

(rf/reg-event-fx
 ::load-pokedex
 (fn [_ _]
   {::make-request {:uri "/pokedex/api/pokemon"
                    :on-success-evt [::got-pokedex]}}))

(rf/reg-sub
 ::pokemon
 (fn [db [_ pokemon-id]]
   (get-in db [:pokemon pokemon-id])))

(rf/reg-event-db
 ::set-pokemon
 (fn [db [_ pokemon-id pokemon]]
   (assoc-in db [:pokemon pokemon-id] pokemon)))

(rf/reg-event-db
 ::set-pokemon-field
 (fn [db [_ pokemon-id field data]]
   (assoc-in db [:pokemon pokemon-id field] data)))

(rf/reg-event-fx
 ::got-pokemon-evolutions
 (fn [_ [_ pokemon-id response]]
   {:fx [[:dispatch [::set-pokemon-field pokemon-id :evolutions (:chain response)]]]}))

(rf/reg-event-fx
 ::load-pokemon-evolutions
 (fn [_ [_ pokemon-id chain-url]]
   {::make-request {:uri chain-url
                    :on-success-evt [::got-pokemon-evolutions pokemon-id]}}))

(rf/reg-event-fx
 ::got-pokemon-specie
 (fn [_ [_ pokemon-id response]]
   {:fx [[:dispatch [::set-pokemon-field pokemon-id :specie response]]
         [:dispatch [::load-pokemon-evolutions pokemon-id
                     (get-in response [:evolution_chain :url])]]]}))

(rf/reg-event-fx
 ::load-pokemon-specie
 (fn [_ [_ pokemon-id specie-url]]
   {::make-request {:uri specie-url
                    :on-success-evt [::got-pokemon-specie pokemon-id]}}))

(rf/reg-event-fx
 ::got-pokemon
 (fn [_ [_ pokemon-id opts response]]
   {:fx
    (cond-> [[:dispatch [::set-pokemon pokemon-id response]]]
      (:load-details? opts)
      (conj [:dispatch [::load-pokemon-specie pokemon-id
                        (get-in response [:species :url])]]))}))

(rf/reg-event-fx
 ::ensure-pokemon-is-loaded
 (fn [{:keys [db]} [_ pokemon-id opts]]
   (if (and (get-in db [:pokemon pokemon-id])
            (not (:load-details? opts)))
     {}
     {::make-request {:uri (str "https://pokeapi.co/api/v2/pokemon/" pokemon-id)
                      :on-success-evt [::got-pokemon pokemon-id opts]}})))

(rf/reg-event-fx
 ::load-and-set-selected-pokemon
 (fn [_ [_ pokemon-id]]
   {:fx [[:dispatch [::ensure-pokemon-is-loaded pokemon-id {:load-details? true}]]
         [:dispatch [::set-selected-pokemon pokemon-id]]]}))

(rf/reg-event-fx
 ::set-history
 (fn [_ [_ opts]]
   {::set-history opts}))

(rf/reg-event-fx
 ::load-app
 (fn [_]
   {:db {}
    :fx [[:dispatch [::load-pokedex]]]}))

(defn- pokemon-image-url
  [pokemon-id]
  (str "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/" pokemon-id ".svg"))

(defn- pokemon-card
  [{:keys [id izena_ingelesez
           izena_euskaraz izena_euskaraz_azalpena] :as _pokedex-entry}]
  (let [show-english? (r/atom false)]
    (fn []
      [:div.pokemon-card
       {:on-click
        (fn [_]
          (swap! show-english? not))
        :class (when @show-english?
                 "pokemon-card--back")}
       (if-not @show-english?
         [:<>
          [:img.pokemon-card__img
           {:src (pokemon-image-url id)}]
          [:span.pokemon-card__id
           (str "#" (.padStart (str id) 3 0))]>
          [:div.pokemon-card__name-container
           [:span.pokemon-card__name
            (str/capitalize izena_euskaraz)]
           [:span.pokemon-card__name-desc
            (str/lower-case izena_euskaraz_azalpena)]]]
         [:<>
          [:span.pokemon-card__name
           (str/capitalize izena_ingelesez)]
          [:span.pokedex__link.pokemon-card__load-pokemon-link
           {:on-click
            (fn [e]
              (.stopPropagation e)
              (rf/dispatch [::load-and-set-selected-pokemon id])
              (rf/dispatch [::set-history {:query-params {"pokemon_id" id}}]))}
           "Informazio gehiago"]])])))

(defn- matches-search?
  [search-text pokemon-entry]
  (if (seq search-text)
    (or
     (str/includes? (get pokemon-entry :izena_euskaraz)
                    (str/lower-case search-text))
     (str/includes? (get pokemon-entry :izena_ingelesez)
                    (str/lower-case search-text))
     (str/includes? (str (get pokemon-entry :id))
                    search-text))
    true))

(defn- pokemon-list
  []
  (let [pokedex (rf/subscribe [::pokedex])
        displayed-count (r/atom 12)
        search-text (r/atom "")]
    (fn []
      (let [filtered-entries (->> @pokedex
                                  (filter (partial matches-search? @search-text)))]
        [:<>
         [:input.pokedex__search-bar
          {:type :text
           :placeholder "Bilatu"
           :value @search-text
           :on-change (fn [e]
                        (reset! search-text (.. e -target -value)))}]
         [:div.pokemon-list
          (for [pokemon-entry (take @displayed-count filtered-entries)]
            ^{:key (str "pokemon_" (:id pokemon-entry))}
            [pokemon-card pokemon-entry])
          (when (< @displayed-count (count filtered-entries))
            [:btn.pokemon-list__load-more-btn
             {:on-click #(swap! displayed-count + 12)}
             "Kargatu gehiago"])]]))))

(defn pokemon-stats-bar
  [stat-n]
  [:div.pokemon-status-graph__bar
   (for [n (reverse (range 1 15))]
     ^{:key (str"pokemon-graph-bar__" n)}
     [:div.pokemon-status-graph__bar-tick
      {:class (when (<= (* n 10) stat-n)
                "pokemon-status-graph__bar-tick--selected")}])])

(defn- pokemon-stats
  [stats]
  [:div.pokemon-entry__section.pokemon-entry__stats
   [:span.pokemon-entry__section-title "Estatistikak"]
   [:div.pokemon-stats-graph
    (for [{:keys [base_stat]
           {:keys [name]} :stat} stats]
      ^{:key (str"pokemon-stats-graph__stat" name)}
      [:div.pokemon-stats-graph__stat
       [:span base_stat]
       [pokemon-stats-bar base_stat]
       [:span (str/capitalize name)]])]])

(defn- pokemon-evolution
  [_evolution]
  (let [pokedex (rf/subscribe [::pokedex])]
    (fn [evolution]
      (if-let [pokedex-entry
               (some #(when (= (:izena_ingelesez %)
                               (get-in evolution [:species :name])) %)
                     @pokedex)]
        [:div.pokemon-evolutions__evolution-container
         [:div.pokemon-evolutions__evolution
          {:on-click (fn []
                       (let [id (:id pokedex-entry)]
                         (rf/dispatch [::load-and-set-selected-pokemon id])
                         (rf/dispatch [::set-history {:query-params {"pokemon_id" id}}])))}
          [:img.pokemon-evolutions__evolution-img
           {:src (pokemon-image-url (:id pokedex-entry))}]
          [:span (str/capitalize (:izena_euskaraz pokedex-entry))]]
         (when (seq (:evolves_to evolution))
           [:div.pokemon-evolutions__evolution-children
            (for [child (:evolves_to evolution)]
              [pokemon-evolution child])])]
        [:div "Errorea"]))))

(defn- pokemon-evolutions
  [evolutions]
  [:div.pokemon-entry__section.pokemon-entry__evolutions
   [:span.pokemon-entry__section-title "Eboluzioak"]
   [:div.pokemon-evolutions
    [pokemon-evolution evolutions]]])

(defn- pokemon-info
  [{:keys [types weight height abilities specie]}]
  [:div.pokemon-entry__section.pokemon-entry__info
   [:span.pokemon-entry__section-title "Informazio orokorra"]
   [:div.pokemon-entry__info-table
    [:div.pokemon-entry__info-field
     [:span "Pisua:"]
     [:span (str (/ weight 10) " kg")]]
    [:div.pokemon-entry__info-field
     [:span "Garaiera:"]
     [:span (/ height 10) " m"]]
    (for [[hidden? abilities] (group-by :is_hidden abilities)]
      ^{:key (str"pokemon-abilities_hidden_" hidden?)}
      [:div.pokemon-entry__info-field
       [:span
        (str
         (cond
           (and hidden? (= 1 (count abilities)))
           "Abilezia ezkutua"
           (and (not hidden?) (= 1 (count abilities)))
           "Abilezia"
           hidden?
           "Abilezia ezkutuak"
           :else
           "Abileziak")
         ": ")]
       [:span (str/join ", " (map (comp :name :ability) abilities))]])
    [:div.pokemon-entry__info-field
     [:span "Arrautzak:"]
     [:span (->> (map :name (:egg_groups specie))
                 (str/join ", "))]]
    [:div.pokemon-entry__info-field
     [:span "Bizilekua"]
     [:span (get-in specie [:habitat :name])]]
    [:div.pokemon-entry__info-field
     [:span "Kolorea:"]
     [:span.pokemon-color
      {:style {:background-color (get-in specie [:color :name])}}
      (get-in specie [:color :name])]]
    [:div.pokemon-entry__info-field
     [:span "Forma:"]
     [:span (get-in specie [:shape :name])]]
    [:div.pokemon-entry__info-field
     [:span "Belaunaldia"]
     [:span (get-in specie [:generation :name])]]
    [:div.pokemon-entry__info-field
     [:span "Mota:"]
     [:div.pokemon-entry__types
      (for [type types
            :let [type-name (get-in type [:type :name])]]
        ^{:keys type-name}
        [:span.pokemon-type.pokemon-entry__type
         {:class (str "pokemon-type--" type-name)}
         type-name])]]]])

(defn- pokedex-entry
  [id]
  (let [pokedex-entry (rf/subscribe [::pokedex-entry id])
        pokemon (rf/subscribe [::pokemon id])]
    (let [{:keys [izena_euskaraz izena_ingelesez]} @pokedex-entry
          {:keys [stats evolutions]} @pokemon]
      [:<>
       [:span.pokedex__link
        {:on-click
         (fn [e]
           (.stopPropagation e)
           (rf/dispatch [::set-selected-pokemon nil])
           (rf/dispatch [::set-history {:query-params {}}]))}
        "Itzuli zerrendara"]
       [:div.pokemon-entry
        [:div.pokemon-entry__header
         [:h1.pokemon-entry__title
          (if izena_euskaraz
            (str (str/capitalize izena_euskaraz)
                 " - "
                 (.padStart (str id) 3 0)
                 " - "
                 (str/capitalize izena_ingelesez))
            "xxx")]]
        [:div.pokemon-entry__section.pokemon-entry__image-container
         [:img.pokemon-entry__image
          {:src (pokemon-image-url id)}]]
        [pokemon-info @pokemon]
        [pokemon-stats stats]
        [pokemon-evolutions evolutions]]])))

(defn- pokedex
  []
  (let [selected-pokemon (rf/subscribe [::selected-pokemon])]
    (fn []
      [:div.pokedex
       (if-let [pokemon-id @selected-pokemon]
         [pokedex-entry pokemon-id]
         [pokemon-list])])))

(defn- root-component []
  [pokedex])

(rdom/render [root-component]
             (.getElementById js/document "pokedex"))

(rf/dispatch [::load-app])

(defn- read-query-params-pokemon
  []
  (let [searcher (js/URLSearchParams. js/window.location.search)]
    (if-let [pokemon-id  (.get searcher "pokemon_id")]
      (rf/dispatch [::load-and-set-selected-pokemon (js/parseInt pokemon-id)])
      (rf/dispatch [::set-selected-pokemon nil]))))

(.addEventListener js/window "popstate" read-query-params-pokemon)

(read-query-params-pokemon)
