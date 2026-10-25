from django.db import models

from exams.models import AssementModel
from accounts.models import User

class QuestionModel(models.Model):

    title =  models.CharField(max_length=200)

    description =  models.TextField()

    score =  models.PositiveIntegerField()

    assesment = models.ForeignKey(AssementModel,on_delete=models.CASCADE)

    smapleinput = models.TextField(null=True)

    sampleoutput = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title