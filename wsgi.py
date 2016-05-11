import sys
import os
import os.path
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    'gamerauntsia')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamerauntsia.settings")
application = get_wsgi_application()
