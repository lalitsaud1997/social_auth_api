from django.urls import path, include
from auth_api import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),

]