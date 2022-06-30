from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    #login-api
    path('login-api/', views.login_api, name='login-api'),
    #login-api
    path('user/', views.get_user_data, name='get-user-data'),
    #register-api
    path('register-api/', views.register_api, name='register-api'),
    #logout
    path('logout/', knox_views.LogoutView.as_view(), name='logout-view'),

    #logoutall
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall-view'),
]