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
    #tasks/
    path('tasks/', views.TasksView.as_view(), name='task-view'),
    #task-create/
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    #task-update/
    path('task-update/<str:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    #task-update/
    path('task-delete/<str:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
]