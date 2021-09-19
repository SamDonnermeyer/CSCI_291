# pages/urls.py

# Imports
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # About Page Templtate
    path('', HomePageView.as_view(), name = 'home'), # Homepage Template
]
