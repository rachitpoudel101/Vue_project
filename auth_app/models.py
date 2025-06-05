from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # You can extend this later with more fields
