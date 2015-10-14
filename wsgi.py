import sys
import os
import os.path
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    'gamerauntsia')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamerauntsia.settings")
# Environment
os.environ['TELEBOT_TOKEN'] = '107547414:AAEXaH2tSNcnaehNq_7NNbNKb1VfDbaa6Qs'
os.environ['MC_CHAT_ID'] = -31046360
os.environ['EDITOR_CHAT_ID'] = -18452263
os.environ['TWITTER_API_KEY'] = 'QMPvaez5H2KpBWP9CwnfYTU2M'
os.environ['TWITTER_API_SECRET'] = 'PIqjFcoSLiaB8RE20KcUjrqI4RAYb8RwzGIfHy43D8zhJttqcc'
os.environ['TWITTER_USERNAME'] = 'gamerauntsia'
os.environ['TWITTER_ACCESS_TOKEN'] = '2663678179-XsYD1snwUqvc7VJryppOPJFbAwO3iFGLsNsaMkE'
os.environ['TWITTER_ACCESS_TOKEN_SECRET'] = 'ZmwQ82fbfIGWY8voHbzfIYKmkT8egMcSOIWGlGE8cZeyD'
os.environ['FB_APP_ID'] = '1466131240329239'
os.environ['FB_APP_SECRET'] = '69cf0d955b37aa12cb0f30857e250fc4'
os.environ['FB_PAGE_ID'] = '326435330850157'
# End Environment
application = get_wsgi_application()
