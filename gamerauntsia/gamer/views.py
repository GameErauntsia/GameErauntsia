from gamerauntsia.gamer.models import GamerUser, JokuPlataforma, PLATFORM
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
from gamerauntsia.gamer.forms import NotifyForm,GameForm
from django.utils.translation import ugettext as _
from django.forms.models import modelformset_factory

def index(request):
    users = GamerUser.objects.filter(is_active=True,is_staff=True).order_by('-date_joined')
    return render_to_response('gamer/index.html', locals(),context_instance=RequestContext(request))
    
def profile(request,username):
    user_prof = get_object_or_404(GamerUser,username=username)
    gameplayak = GamePlaya.objects.filter(publikoa_da=True,erabiltzailea=user_prof).order_by('-pub_date')
    gp_count = len(gameplayak)
    categs = GamePlaya.objects.filter(publikoa_da=True,erabiltzailea=user_prof).values('kategoria__izena',).annotate(count=Count('id'))
    berriak = Berria.objects.filter(publikoa_da=True,erabiltzailea=user_prof).order_by('-pub_date')
    bcategs = Berria.objects.filter(publikoa_da=True,erabiltzailea=user_prof).values('gaia__izena',).annotate(count=Count('id'))
    berri_count = len(berriak)
    side_berriak = berriak[:5]
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))

def guestprofile(request,username):
    user_prof = get_object_or_404(GamerUser,username=username,is_active=True)
    if user_prof.is_staff:
        return HttpResponseRedirect('/nor-gara/'+username)
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))


def community(request):
    users = GamerUser.objects.filter(is_active=True)
    return render_to_response('gamer/community.html', locals(),context_instance=RequestContext(request))


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
            return HttpResponseRedirect(reverse('edit_profile_noti'))
    else:
        notifyform = NotifyForm(instance=user)

    return render_to_response('profile/edit_notifications.html', locals(), context_instance=RequestContext(request))

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