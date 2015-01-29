from gamerauntsia.gamer.models import GamerUser, JokuPlataforma, PLATFORM
from django.template.defaultfilters import slugify
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gamerauntsia.utils.images import handle_uploaded_file
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from photologue.models import Photo
from gamerauntsia.gamer.forms import *
from django.utils.translation import ugettext as _
from django.forms.models import modelformset_factory
from datetime import datetime
from django.db.models import Count
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordChangeForm
from django.template.response import TemplateResponse
from django_simple_forum.models import Category
from django.utils import timezone

def update_session_auth_hash(request, user):
    """
    Updating a user's password logs out all sessions for the user if
    django.contrib.auth.middleware.SessionAuthenticationMiddleware is enabled.
    This function takes the current request and the updated user object from
    which the new session hash will be derived and updates the session hash
    appropriately to prevent a password change from logging out the session
    from which the password was changed.
    """
    if hasattr(user, 'get_session_auth_hash') and request.user == user:
        request.session[HASH_SESSION_KEY] = user.get_session_auth_hash()

def index(request):
    users = GamerUser.objects.filter(is_active=True,is_staff=True).order_by('-date_joined')
    return render_to_response('gamer/index.html', locals(),context_instance=RequestContext(request))

def profile(request,username):
    user_prof = get_object_or_404(GamerUser,username=username)
    gameplayak = GamePlaya.objects.filter(publikoa_da=True,status='1', erabiltzailea=user_prof, pub_date__lt=datetime.now()).order_by('-pub_date')
    gp_count = len(gameplayak)
    categs = GamePlaya.objects.filter(publikoa_da=True, status='1', erabiltzailea=user_prof, pub_date__lt=datetime.now()).values('kategoria__izena',).annotate(count=Count('id'))
    berriak = Berria.objects.filter(publikoa_da=True, status='1', erabiltzailea=user_prof,pub_date__lt=datetime.now()).order_by('-pub_date')
    bcategs = Berria.objects.filter(publikoa_da=True, status='1', erabiltzailea=user_prof,pub_date__lt=datetime.now()).values('gaia__izena',).annotate(count=Count('id'))
    berri_count = len(berriak)
    side_berriak = berriak[:5]
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))

def guestprofile(request,username):
    user_prof = get_object_or_404(GamerUser,username=username,is_active=True)
    if user_prof.is_staff:
        return HttpResponseRedirect('/nor-gara/'+username)
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))


def community(request):
    users = GamerUser.objects.filter(is_active=True).order_by('-date_joined')[:9]
    gurus = GamerUser.objects.filter(is_active=True,is_staff=False).order_by('-karma','-date_joined')[:9]
    return render_to_response('gamer/community.html', locals(),context_instance=RequestContext(request))

@login_required
def edit_profile(request):
    """ """
    tab = 'personal'
    profile = request.user
    if request.method == 'POST':
         profileform = GamerForm(request.POST, instance=profile)
         if profileform.is_valid():
            profileform.save()
            messages.add_message(request, messages.SUCCESS, _('New user data saved.'), fail_silently=True)
    else:
        profileform = GamerForm(instance=profile)

    return render_to_response('profile/edit_personal.html', locals(), context_instance=RequestContext(request))

@login_required
def edit_notifications(request):
    """ """
    tab = 'notifications'
    user = request.user
    if request.method == 'POST':
         posta=request.POST.copy()
         notifyform = NotifyForm(posta, instance=user)
         if notifyform.is_valid():
            notifyform.save()
    else:
        notifyform = NotifyForm(instance=user)

    return render_to_response('profile/edit_notifications.html', locals(), context_instance=RequestContext(request))

@login_required
def edit_computer(request):
    """ """
    tab = 'computer'
    user = request.user
    if request.method == 'POST':
         posta=request.POST.copy()
         pcform = PCForm(posta, instance=user)
         if pcform.is_valid():
            pcform.save()
            return HttpResponseRedirect(reverse('edit_profile_comp'))
    else:
        pcform = PCForm(instance=user)

    return render_to_response('profile/edit_computer.html', locals(), context_instance=RequestContext(request))


@login_required
def edit_platform(request):
    """ """
    tab = 'platforms'
    user = request.user
    GameFormSet = modelformset_factory(JokuPlataforma, form=GameForm, can_delete=True)
    if request.method == 'POST':
         posta=request.POST.copy()
         gameformset = GameFormSet(posta)
         if gameformset.is_valid():
            marked_for_delete = gameformset.deleted_forms
            for form in gameformset:
                if form.is_valid() and form.has_changed():
                    if form['id'].value() in [deleted_record['id'].value() for deleted_record in marked_for_delete]:
                        platform = form.save(commit=False)
                        platform.delete()
                    else:
                        platform = form.save(commit=False)
                        platform.user = user
                        platform.save()
            return HttpResponseRedirect(reverse('edit_profile_plat'))
    else:
        qset = JokuPlataforma.objects.filter(user=user)
        gameformset = GameFormSet(queryset=qset)
        options = PLATFORM

    return render_to_response('profile/edit_platform.html', locals(), context_instance=RequestContext(request))


@login_required
def edit_top_games(request):
    """ """
    tab = 'top_games'
    user = request.user
    if request.method == 'POST':
         posta=request.POST.copy()
         topform = TopForm(posta, instance=user)
         if topform.is_valid():
            topform.save()
            return HttpResponseRedirect(reverse('edit_profile_top'))
    else:
        topform = TopForm(instance=user)
        lagunak = GamerUser.objects.filter(top_jokoak__in=user.top_jokoak.all()).exclude(id=user.id).distinct().order_by('-karma')[:15]
        topjokoak = GamerUser.objects.values('top_jokoak__izena').annotate(Count('top_jokoak')).order_by('-top_jokoak__count','-top_jokoak__izena')[:10]

    return render_to_response('profile/edit_top_games.html', locals(), context_instance=RequestContext(request))

@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('edit_profile_pass_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': _('Password change'),
        'tab': 'pass',
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@login_required
def password_change_done(request,
                         template_name='registration/password_change_done.html',
                         current_app=None, extra_context=None):
    context = {
        'title': _('Password change successful'),
        'tab': 'pass',
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

@login_required
def lastlogin(request):
    """ """
    user = request.user
    if request.method == 'POST':
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        return HttpResponseRedirect(reverse('forum-index'))
    else:
        lastloginform = LastloginForm(instance=user)

    categories = Category.objects.all().order_by('order')
    return render_to_response("django_simple_forum/list.html", {'categories': categories,
                                'user': request.user},
                                context_instance=RequestContext(request))


@login_required
def add_article(request):
    """ """
    user = request.user
    if request.method == 'POST':
        articleform = ArticleForm(request.POST)
        if articleform.is_valid():
            berria = articleform.save(commit=False)
            berria.slug = slugify(berria.izenburua)
            berria.erabiltzailea = user
            if request.FILES.get('argazkia',''):
                photo = handle_uploaded_file(request.FILES['argazkia'], user.getFullName())
                berria.argazkia = photo
            berria.save()
            articleform.save_m2m()
            return render_to_response('profile/article_sent.html', locals(), context_instance=RequestContext(request))
    else:
        articleform = ArticleForm()
    return render_to_response('profile/add_article.html', locals(), context_instance=RequestContext(request))

@login_required
def add_gameplay(request):
    """ """
    user = request.user
    if request.method == 'POST':
        gameplayform = GamePlayForm(request.POST,request.FILES)
        if gameplayform.is_valid():
            gp = gameplayform.save(commit=False)
            gp.slug = slugify(gp.izenburua)
            gp.erabiltzailea = user
            gp.argazkia = handle_uploaded_file(request.FILES['argazkia'], user.getFullName())
            gp.save()
            gameplayform.save_m2m()
            return render_to_response('profile/gameplay_sent.html', locals(), context_instance=RequestContext(request))
    else:
        gameplayform = GamePlayForm()
    return render_to_response('profile/add_gameplay.html', locals(), context_instance=RequestContext(request))
