from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social_auth/', include('auth_api.urls'), name="social_auth"),
]
