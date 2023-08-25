"""
WSGI config for diana_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from diana_portfolio import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diana_portfolio.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

