from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from accounts.serailizers import UserSerializer
from accounts.models import User
from accounts.models import StudentProfile
from accounts.serailizers import StudentProfileSerializer

from evaluation.permissons import IsStudent

class AdminCreateViwe(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data= form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_superuser(role="admin",**cleaned_data)

            serializer = UserSerializer(instance)

            return Response(data=serializer.data)

        else:return Response(data=serializer.errors)

class StudentCreateView(APIView):

    def post(self,requset):

        from_data = requset.data

        serializer = UserSerializer(data= from_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer = UserSerializer(instance)

            return Response(data=serializer.data)

        else:

            return Response(data=serializer.errors)



class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudent]

    def put(self,request):

        form_data = request.data

        student_profile_object = StudentProfile.objects.get(student=request.user)

        serilaize_instance = StudentProfileSerializer(data=form_data,instance=student_profile_object)

        if serilaize_instance.is_valid():

            serilaize_instance.save()

            return Response(data=serilaize_instance.data)

        else:return Response(data=serilaize_instance.errors)

class GetMeView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsStudent]

    def get(self,request):

        user = request.user        

        instance = get_object_or_404(StudentProfile,student=user)

        serializer_instance = StudentProfileSerializer(instance)

        return Response(data= serializer_instance.data)