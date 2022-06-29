import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #api/
    path('api/', include('to_do.urls')),
    #Home page
    path('', include('frontend.urls')),
]
