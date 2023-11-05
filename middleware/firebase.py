from core.models import User
import jwt
from django.utils.functional import SimpleLazyObject
from rest_framework.response import Response
from rest_framework import status
import time


class FirebaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        def _get_user():
            auth_header = request.META.get("HTTP_AUTHORIZATION")
            if auth_header:
                _, token = auth_header.split()

                try:
                    decoded_token = jwt.decode(
                        token,
                        algorithms=["RS256"],
                        options={"verify_signature": False},
                    )
                    user_id = decoded_token["uid"]
                    expiry_time = decoded_token["exp"]
                    current_time = time.time()
                    if current_time > expiry_time:
                        return None
                    else:
                        user = User.objects.get(id=user_id)
                        request.authUser = user
                except Exception as e:
                    user = None
            else:
                user = None
            return user

        request.authUser = SimpleLazyObject(_get_user)
        if request.authUser is None:
            return Response(
                {"message": "User is not authorized or the token has expired"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        response = self.get_response(request)
        return response
