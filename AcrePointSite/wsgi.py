import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AcrePointSite.settings')

application = get_wsgi_application()
