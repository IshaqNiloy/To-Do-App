from django.shortcuts import render

# Create your views here.

def view_list(request):
    return render(request, 'frontend/list.html')
