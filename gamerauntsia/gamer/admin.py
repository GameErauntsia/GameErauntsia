from django.contrib import admin
from gamerauntsia.gamer.models import GamerUser
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import AdminPasswordChangeForm,UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from django import forms


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
        #fields = ('email', )

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

    form = MyUserChangeForm
    change_user_password_template = None
    add_form = MyUserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('username','fullname','get_email','is_staff')

    list_display_links = ('fullname','username')
    search_fields = ['email','username','fullname']
    raw_id_fields = ('photo',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        ('Datuak',
        {'fields':('fullname','nickname','email', 'phone', 'photo','bio')},),
        ('Sare sozialak',
        {'fields':('ytube_channel','twitter_id', 'facebook_id', 'openid_id', 'googleplus_id'),'classes': ['collapse',],},),
        ('Mota',
        {'fields':('usertype',  'added_source'),'classes': ['collapse',],},),
        (_('Permissions'), {'fields': ('is_active','is_gamer', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions','last_login'),
                            'classes': ['collapse',],}),

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
        qs = super(GamePlayAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id = request.user.id)

admin.site.register(GamerUser,GamerUserAdmin)
