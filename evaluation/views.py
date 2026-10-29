from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import serializers


from exams.models import AssementModel

from problem.models import QuestionModel

from evaluation.permissons import IsStudent
from evaluation.models import Submission
from evaluation.serilaizer import SubmissionSerializers
from evaluation.serilaizer import AnswerSerializer




class SubmissionStartView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_object = get_object_or_404(AssementModel,id=assessment_id)

        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializers_instance = SubmissionSerializers(instance)

        return Response(data=serializers_instance.data)

class SubmissionListing(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudent]

    serializer_class = SubmissionSerializers

    queryset = Submission.objects.all()
    
    
class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudent]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        # validtion start

        assesment_object = submission_object.assessment

        assessment_questions = QuestionModel.objects.filter(assesment=assesment_object).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_questions:

            raise serializers.ValidationError("Invalid question,question not exisiting")


        # validation end

        serializer_instance = AnswerSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission=submission_object)

            return Response(data=serializer_instance.data)

        else:return Response(data=serializer_instance.errors)


class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        instantce = get_object_or_404(Submission,id=pk)

        serializer_instantce = SubmissionSerializers(instantce)

        return Response(data=serializer_instantce.data)

