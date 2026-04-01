import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glorp.settings")  # change "myproject" to your project folder name

application = get_wsgi_application()