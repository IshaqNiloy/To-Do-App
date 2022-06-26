import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #to-do/
    path('', include('to_do.urls')),
]
