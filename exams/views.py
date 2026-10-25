from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from exams.models import AssementModel
from exams.serializers import AssementSerializer
from exams.permission import IsOwner

from datetime import time,timedelta,datetime

class ExamListCreate(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = AssementModel.objects.all()

        serializer = AssementSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = AssementSerializer(data = form_data)

        if serializer.is_valid(): 

            serializer.save(created_by=request.user)

            # cleaned_data = serializer.validated_data

            # cleaned_data.pop("start_time")

            # exam_date = cleaned_data["exam_date"]

            # last_exam_object = AssementModel.objects.filter(created_by=request.user,exam_date=exam_date).order_by("start_time").last()

            # if last_exam_object:

            #     start_time = datetime.combine(exam_date, last_exam_object.end_time) + timedelta(hours=1)

            # else:

            #     start_time = datetime.combine(exam_date,time(9,0))

            # exam_end_time = start_time + timedelta(minutes=cleaned_data["duration"])
            
            # # The model stores clock times, so persist only the time portion.
            # qs = AssementModel.objects.create(**cleaned_data,created_by=request.user,start_time=start_time.time(),end_time=exam_end_time.time())

            # serializer = AssementSerializer(qs)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)


class ExamRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        instance = get_object_or_404(AssementModel,id=pk)

        self.check_object_permissions(request,instance)

        serializer = AssementSerializer(instance)

        return Response(data=serializer.data)

    def put (self,request,pk=None):

        instance = get_object_or_404(AssementModel,id=pk)

        form_data = request.data

        serilaizer = AssementSerializer(data=form_data,instance=instance)

        if serilaizer.is_valid():

            serilaizer.save()

            return Response(data=serilaizer.data)

        else:return Response(data=serilaizer.errors)

    def delete(self,requset,pk=None):

        instance = get_object_or_404(AssementModel,id=pk)

        instance.delete()

        response_data = {"message":"deleted"}

        return Response(data=response_data)






