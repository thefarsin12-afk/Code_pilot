from django.db import models

from exams.models import AssementModel
from accounts.models import User



class QuestionModel(models.Model):

    title =  models.CharField(max_length=200)

    description =  models.TextField()

    score =  models.PositiveIntegerField()

    assesment = models.ForeignKey(AssementModel,on_delete=models.CASCADE)

    smapleinput = models.TextField(null=True)

    sampleoutput = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    qeustion_number = models.PositiveIntegerField(null=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title


    def save(self,*args,**kwargs):

        last_object = QuestionModel.objects.filter(assesment=self.assesment).last()

        if last_object:

            self.qeustion_number = last_object.qeustion_number + 1

        else:
            
            self.qeustion_number = 1

        return super().save(*args,**kwargs)