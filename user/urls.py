from django.urls import path
# from knox import views as knox_views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #register/
    path('register/', views.RegisterView.as_view(), name='register'),
    #api/token/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #api/token/refresh/
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #login-api/
    path('login/', views.LoginView.as_view(), name='login-api'),
    #login-api/
    # path('user/', views.get_user_data, name='get-user-data'),
]