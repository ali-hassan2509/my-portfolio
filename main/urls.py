# main/urls.py (Create this file)

from django.urls import path
from .views import home_view

urlpatterns = [
    # The name 'home' is used in the view's redirect
    path('', home_view, name='home'),
]