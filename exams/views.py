from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from exams.models import AssementModel
from exams.serializers import AssementSerializer

class ExamListCreate(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance = AssementModel.objects.all()

        serializer = AssementSerializer(instance,many=True)

        return Response(data=serializer.data)


