from django.contrib import admin
from gamerauntsia.gamer.models import GamerUser, JokuPlataforma
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import AdminPasswordChangeForm,UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from django import forms

class PlataformaInline(admin.TabularInline):
    model = JokuPlataforma
    fields = ('plataforma','nick')



class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = GamerUser

class MyUserCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = GamerUser
        exclude = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MyUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class GamerUserAdmin(UserAdmin):

    def admin_thumbnail(self,obj):
        try:
            if obj.get_photo():
                return u'<img src="%s" />' % (obj.get_photo().get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.get_photo().title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    def preview(self,obj):
        return '<a href="/komunitatea/%s">aurreikusi</a>' % (obj.username)
    preview.allow_tags=True

    form = MyUserChangeForm
    change_user_password_template = None
    add_form = MyUserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('admin_thumbnail','username','fullname','preview','get_email','is_gamer','is_staff','is_active','date_joined')
    list_display_links = ('fullname','username')
    list_filter = ('is_staff', 'is_gamer','is_superuser', 'is_active', 'buletin_notification', 'groups')
    search_fields = ['email','username','fullname']
    raw_id_fields = ('photo',)

    inlines = [PlataformaInline]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        ('Datuak',
        {'fields':('fullname','nickname','karma','email','phone', 'photo','bio','signature')},),
        ('Ordenagailua',
        {'fields':('motherboard','processor','graphics','soundcard','ram','harddrive','harddrive2','mouse','keyboard','speakers')},),
        ('Jakinarazpenak',
        {'fields':('email_notification','buletin_notification')},),
        ('Sare sozialak',
        {'fields':('ytube_channel','twitch_channel','twitter_id', 'facebook_id', 'telegram_id'),'classes': ['collapse',],},),
        (_('Permissions'), {'fields': ('is_active','is_gamer', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions','last_login'),
                            'classes': ['collapse',],}),

    )

    restricted_fieldsets = (
        (None, {'fields': ('username', 'password')}),

        ('Datuak',
        {'fields':('fullname','nickname','email', 'phone', 'photo','bio')},),
        ('Sare sozialak',
        {'fields':('ytube_channel','twitter_id', 'facebook_id', 'openid_id', 'googleplus_id'),'classes': ['collapse',],},),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )

    def get_email(self, obj):
        """ """
        return obj.email

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(GamerUserAdmin, self).get_form(request, obj, **defaults)

    def queryset(self, request):
        qs = super(GamerUserAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id = request.user.id)

    #def get_fieldsets(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return self.fieldsets
    #    return self.restricted_fieldsets

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True # So they can see the change list page
        if request.user.is_superuser or obj.id == request.user.id:
            return True
        else:
            return False
    has_delete_permission = has_change_permission

admin.site.register(GamerUser,GamerUserAdmin)
