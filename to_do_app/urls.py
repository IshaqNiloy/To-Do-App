import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #api/
    path('api/', include('to_do.urls')),
    #Home page
    path('', include('frontend_user.urls')),
    #user-api/
    path('user-api/', include('user.urls')),
]
