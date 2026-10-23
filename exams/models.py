from django.db import models

from accounts.models import User

class AssementModel(models.Model):

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=100)

    LANGUAGE_CHOISES = {

            ("PYTHON","python"),
            ("DJANGO","django"),
            ("REACT.JS","react.js"),

    }
    
    language= models.CharField(max_length=100,choices=LANGUAGE_CHOISES,default="pending")

    exam_date= models.DateField()

    duration = models.PositiveIntegerField()

    start_time= models.DateTimeField()

    end_time = models.DateTimeField(null=True,blank=True)
    
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    STATUS_CHOISES = {

            ("PENDING","pending"),
            ("IN PROGRESS","in progress"),
            ("COMPLETED","completed"),
    }

    status = models.CharField(max_length=100,choices=STATUS_CHOISES,default="IN_PROGRESS")

    def __str__(self):

            return self.title