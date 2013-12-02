"""
WSGI config for django_crud_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_crud_app.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from dj_static import Cling
application = Cling(get_wsgi_application())

# Bind to PORT if defined, otherwise default to 5000.
# port = int(os.environ.get('PORT', 5000))
# notes.run(host='0.0.0.0', port=port)	