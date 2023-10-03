from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

from core.views import front, portfolio, biography, services, clients, send_contact_email

urlpatterns = [
    path('', front, name="index"),
    path('portfolio/', portfolio, name='portfolio'),
    path('biography/', biography, name='biography'),
    path('services/', services, name='services'),
    path('clients/', clients, name='clients'),
    path('contact/', send_contact_email, name='send_contact_email'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)