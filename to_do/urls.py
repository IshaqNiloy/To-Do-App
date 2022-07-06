from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    #task-list/
    path('task-list/', views.task_list, name='task-list'),
    #task-create/123
    path('task-create/', views.task_create, name='task-create'),
    #task-delete
    path('task-delete/<str:pk>', views.task_delete, name='task-delete'),
    #task-detail/123/
    # path('task-detail/<str:pk>', views.task_detail, name='task-detail'),
    #task-update
    # path('task-update/<str:pk>', views.task_update, name='task-updte'),
]