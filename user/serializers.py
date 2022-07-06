from dataclasses import fields
from typing_extensions import Required
from django.contrib.auth.models import User
import jwt
from pkg_resources import require
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
import jwt, datetime

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

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def authorization(self, validated_data):
        try:    
            user = User.objects.filter(email = validated_data['email']).first()
            if user:
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.datetime.utcnow(minutes = 60),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, 'SECRET_KEY', algorithm='HS256').decode('utf-8')

                return Response({
                    'jwt': token
                })
        except KeyError:
            res = {'error': 'Please provide an email and a password'}
            return Response(res)















