from http.client import ResponseNotReady
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'Task Create': '/task-create/',
        'Task Detail': '/task-detail/<str:pk>.',
        'Task Upadate': '/task-update/<str:pk>',
        'Task Delete': '/task-delete/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)