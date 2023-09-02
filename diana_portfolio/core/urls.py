from django.urls import path
from django.contrib.auth import views

from core.views import front, portfolio

urlpatterns = [
    path('', front, name="index"),
    path('portfolio/', portfolio, name="portfolio"),
]