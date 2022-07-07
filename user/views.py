import imp
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import redirect, render
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers, validators, status

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
    permission_classes = (AllowAny,)

    def something(self) -> bool:
        return "something"

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.data['token']
            return Response({"token": serializer.data['token']}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        


    # def get_queryset(self):
    #     print("asdasdasd")
    #     return User.objects.all(id=1)
    # serializer_class.authorization()