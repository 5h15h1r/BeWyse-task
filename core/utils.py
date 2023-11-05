from django.contrib.auth.models import User
import random
import string


def generate_unique_usernames(email):
    username = email.split("@")[0] + "".join(
        random.choices(string.digits, k=4)
    )
    while User.objects.filter(username=username).exists():
        username += random.choice(string.digits)
    return username


def get_full_name(first_name, last_name):
    if first_name is None or last_name is None:
        return ""
    else:
        return f"{first_name}-{last_name}"
