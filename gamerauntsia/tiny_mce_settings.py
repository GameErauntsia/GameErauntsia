TINYMCE_BODY_CONFIG = {
    "selector": "textarea",
    "theme": "modern",
    "plugins": [
            "advlist autolink lists link image charmap print preview anchor",
            "searchreplace visualblocks code fullscreen",
            "insertdatetime media table contextmenu paste"
        ],
    "toolbar": "styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | preview"
    "height" : "300px"
}

TINYMCE_SMALL_BODY_CONFIG = {
    #mode : "textareas",
    "mode" : "exact",
    "elements" : "body",
    "convert_urls" : False,
    "theme" : "modern",
    "theme_advanced_buttons1" : "formatselect,bold,italic,underline,separator,bullist,numlist,blockquote,undo,redo,link,unlink,image,code,removeformat,cut,copy,paste,pastetext,pasteword,selectall,pastetext,",
    "theme_advanced_buttons2" : "",
    "theme_advanced_buttons3" : "",
    "theme_advanced_toolbar_location" : "top",
    "theme_advanced_toolbar_align" : "left",
    "plugins" : "paste, autoresize",
    "paste_auto_cleanup_on_paste" : True,
    "paste_use_dialog" : False,
    "forced_root_block" : "",
    "force_br_newlines" : True,
    "force_p_newlines" : False,
    "content_css" : "/static/css/stylehtmleditor.css",
    "extended_valid_elements" : "object[width|height|classid|codebase],param[name|value],embed[src|type|width|height|flashvars|wmode],iframe[src|name|width|height|align|frameborder|marginwidth|marginheight|scrolling],audio[controls=],source[src|type]",
    'theme_advanced_resizing' : True,
}
