from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication


from exams.models import AssementModel

from evaluation.permissons import IsStudent
from evaluation.models import Submission
from evaluation.serilaizer import SubmissionSerializers

class SubmissionStartView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk):

        assessment_id = pk

        assessment_object = get_object_or_404(AssementModel,id=assessment_id)

        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializers_instance = SubmissionSerializers(instance)

        return Response(data=serializers_instance.data)

    
    





