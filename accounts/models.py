from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length=200)

    ROLE_CHOISES = {

        ("student","student"),
        ("admin","admin")
    }

    role = models.CharField(max_length=200,choices=ROLE_CHOISES,default="student")