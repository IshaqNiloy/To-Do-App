from dataclasses import fields
from json import tool
from typing_extensions import Required
from to_do_app import settings
from django.contrib.auth.models import User
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from pkg_resources import require
from rest_framework import serializers, validators, status
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
import jwt, datetime
from django.contrib.auth import authenticate
from to_do.models import Task


class TaskSerializer(serializers.ModelSerializer):
    # user_username = serializers.RelatedField(source='user.username', read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset = User.objects.all())]
    )

    password1 = serializers.CharField(write_only = True, required = True, validators=[validate_password])
    password2 = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"Password": "Password fields didn't match!"})
        
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    access_token = serializers.CharField(required=False)
    refresh_token = serializers.CharField(required=False)

    # class Meta:
    #     model = User
    #     fields = ('email', 'password')

    def validate(self, validated_data):
        try:    
            user = authenticate(username=validated_data['username'], password=validated_data['password'])
            if user:
                token = RefreshToken.for_user(user)
                validated_data['access_token'] = token.access_token
                validated_data['refresh_token'] = token

                return validated_data

        except KeyError:
            res = {'error': 'Please provide an email and a password'}
            return Response(res)















