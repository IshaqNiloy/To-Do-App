from django.urls import path
from . import views

urlpatterns = [
    #login
    path('login/', views.login, name='login'),
    #logout
    path('logout/', views.logout, name='logout'),
    #register
    path('register/', views.register, name='register'),
]