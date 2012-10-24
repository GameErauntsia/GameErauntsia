from django import forms
from tutorialak.models import Tutoriala
from tinymce.widgets import TinyMCE

class TutorialAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs={                    
                    'theme' : "advanced",
                    'extended_valid_elements' : "iframe[src|width|height|name|align]",
                    'theme_advanced_buttons1' : "formatselect,bold,italic,underline,separator,justifyleft,justifycenter,justifyright, justifyfull,bullist,numlist,undo,redo,link,unlink,image,code,removeformat",
                    'theme_advanced_buttons2' : "",
                    'theme_advanced_buttons3' : "",
                    'theme_advanced_toolbar_location' : "top",
                    'theme_advanced_toolbar_align' : "left",
                    'theme_advanced_resizing' : 'false',
                    'forced_root_block' : '',
                    }))

    class Meta:
        model = Tutoriala	