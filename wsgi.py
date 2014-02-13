import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'rapidsms_tut')))
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rapidsms_tut.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'rapidsms_tut.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 


