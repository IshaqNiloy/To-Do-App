from django.urls import path
# from knox import views as knox_views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #login-api/
    path('login-api/', views.login_api, name='login-api'),
    #login-api/
    path('user/', views.get_user_data, name='get-user-data'),
    #register-api/
    path('register-api/', views.register_api, name='register-api'),
    # #logout/
    # path('logout/', knox_views.LogoutView.as_view(), name='logout-view'),
    # #logoutall
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall-view'),
    #api/token/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #api/token/refresh/
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]