from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    full_name = serializers.CharField(allow_blank=True)


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class LoginSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
