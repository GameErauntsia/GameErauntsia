TINYMCE_DEFAULT_CONFIG = {
    "language": 'eu',
    "theme": "modern",
    "height": 600,
    "plugins": [
        "advlist autolink lists link image charmap print preview anchor",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime media table contextmenu paste",
    ],
    "toolbar": "styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | code preview",
    "menubar": False,
    "media_alt_source": False,
    "media_poster": False,
    "media_dimensions": False,
    "content_css": "/static/css/tinymce_content.css",
}

TINYMCE_SMALL_BODY_CONFIG = {
    "language": 'eu',
    "theme": "modern",
    "plugins": [
        "advlist autolink lists link image charmap print preview anchor",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime media table contextmenu paste",
    ],
    "toolbar": "styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | preview",
    "theme_advanced_resizing": True,
}
