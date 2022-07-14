from ast import Is
import imp
from multiprocessing import AuthenticationError
from to_do_app import settings
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import redirect, render
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers, validators, status
import jwt
from to_do.models import Task
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

@api_view(['POST'])
def register(request):
    return render(request, 'user/register.html')

@api_view(['POST'])

# def login_api(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     _, token = AuthToken.objects.create(user)

#     return Response({
#         'user_info': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email 
#         },
#         'token': token
#     })

def logout(request):
    pass

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email 
        },
    })

    else:
        return Response({'error': 'Not Authenticated!'}, status=400)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        try:
            if serializer.is_valid():
                token = serializer.data['token']
                response = Response({"Message": "Logged in successfully!"}, status=status.HTTP_200_OK)
                response.set_cookie(key='jwt', value=token, httponly=True)
                response.data = {
                    'jwt': token
                }
            return response
        except Exception as e:
            return Response({"message": "Wrong Username or Password! Please try again."}, status=status.HTTP_400_BAD_REQUEST)
        


class TasksView(APIView):
    # permission_classes = [IsAuthenticated,]
    # authentication_class = JWTAuthentication

    def get(self, request):
        # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwidXNlcm5hbWUiOiJ1c2VyNSJ9.Rm6WciPJxc3X2gTuPpH23oog3JmKl9UyFc9eke618qY'
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # print(payload)
        # return Response({"msg": 'hello'}, 200)
        if not token:
            raise AuthenticationError('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationError('Unauthenticated!!')
        print(payload['username'])
        tasks = Task.objects.filter(user__username=payload['username'])
        # tasks.user.fullname
        # print('tasks.user.username =========================== ', tasks)


        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)
