# blog/urls.py
from django.urls import path
from .views import BlogListView

# url pattern
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]