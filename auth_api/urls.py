from django.urls import path
from auth_api import views

urlpatterns = [
    path( '', views.home, name='home'),
]