from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    pass

def register(request):
    pass
