from django.db import models

from django.contrib.auth.models import AbstractUser

# post save calling
from django.db.models.signals import post_save

# send mail importing 
from django.core.mail import send_mail

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length=200)

    ROLE_CHOISES = {

        ("student","student"),
        ("admin","admin")
    }

    role = models.CharField(max_length=200,choices=ROLE_CHOISES,default="student")


class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passoutyear = models.CharField(max_length=20,null=True)

    githuburl = models.URLField(null=True)

    linkedurl = models.URLField(null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student") 

# student profile auto creating 
def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

# signal connecting
post_save.connect(create_student_profile,sender=User)       

# auto email genartaing section
def send_inviation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        send_mail(
            "Account creating conferamtion",
            "You have created account in codepilote.",
            "thefarsin12@gmail.com",
            ["ayushnandakumar04@gmail.com"],
    )

post_save.connect(send_inviation_mail,sender=User)






