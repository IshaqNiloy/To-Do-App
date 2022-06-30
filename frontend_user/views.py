from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'frontend_user/login.html')

def logout(request):
    # return render(request, 'frontend_user/login.html')
    pass

def register(request):
    return render(request, 'frontend_user/register.html')