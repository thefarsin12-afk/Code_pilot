from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from problem.serialiserz import QuestionSerilaizer
from problem.models import QuestionModel

from exams.models import AssementModel


class QuestionCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_object = AssementModel.objects.get(id=assessment_id)

        form_data = request.data

        serializer_instants = QuestionSerilaizer(data=form_data)

        if serializer_instants.is_valid():

            serializer_instants.save(assesment=assessment_object,created_by=request.user)

            return Response(data=serializer_instants.data)

        else:return Response(data=serializer_instants.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = QuestionSerilaizer

    queryset = QuestionModel.objects.all()

    
