# pages/view.py

# Imports
from django.shortcuts import render
from django.views.generic import TemplateView

# Create Class #
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
