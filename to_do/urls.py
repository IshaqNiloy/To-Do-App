from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    #task-list
    path('task-list/', views.task_list, name='task-list')
]