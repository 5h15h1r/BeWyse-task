from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    full_name = serializers.CharField()


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class LoginSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")


class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "full_name")
