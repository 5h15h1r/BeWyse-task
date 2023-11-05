from django.urls import path
from .views import RegisterView, LoginView, ViewProfile, UpdateProfile

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/view/", ViewProfile.as_view()),
    path("profile/edit/", UpdateProfile.as_view()),
]
