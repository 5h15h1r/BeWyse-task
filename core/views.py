from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .utils import generate_unique_usernames, get_full_name
from .models import User
from .serializers import (
    LoginSerialzer,
    RegisterSerializer,
    UserSerializer,
)


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"message": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        validator = MinimumLengthValidator(min_length=8)

        try:
            validator.validate(password)
        except ValidationError as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            username = request.data.get("username")
            if not username:
                username = generate_unique_usernames(email)
                user.username = username
            user.set_password(password)
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):
    def post(self, request):
        data = request.data
        serialzer = LoginSerialzer(data=data)
        if serialzer.is_valid():
            username = serialzer.data["username"]
            password = serialzer.data["password"]

            if not username or not password:
                return Response(
                    {"message": "Username and password are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.get(username=username)
            if user is not None and user.check_password(password):
                custom_token = auth.create_custom_token(str(user.id))
                username = user.username
                email = user.username
                fullname = ""
                loginData = {
                    "username": username,
                    "email": email,
                    "full_name": fullname,
                    "token": custom_token,
                }
                return Response(
                    loginData,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Username or password is invalid"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )


class ViewProfile(APIView):
    def get(self, request):
        username = request.data.get("username")
        user = request.user
        allUsers = User.objects.all()
        if user not in allUsers:
            return Response(
                {"message": "User not authorized"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.username != username:
            return Response(
                {
                    "message": f"User with the username {username} does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = user.username
        email = user.email
        full_name = get_full_name(user.first_name, user.last_name)
        viewData = {
            "username": username,
            "email": email,
            "full_name": full_name,
        }
        serializer = UserSerializer(data=viewData)
        if serializer.is_valid():
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


@method_decorator(csrf_exempt, name="dispatch")
class UpdateProfile(APIView):
    def post(self, request):
        username = request.data.get("username")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        user = request.user
        print(user)
        allUsers = User.objects.all()
        if user not in allUsers:
            return Response(
                {"message": "User not authorized"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user is not None:
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.first_name = first_name
            if username is not None:
                user.first_name = first_name
            full_name = get_full_name(user.first_name, user.last_name)
            data = {
                "username": user.username,
                "email": user.email,
                "full_name": full_name,
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_200_OK,
                )
