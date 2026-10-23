from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from exams.views import ExamListCreate


urlpatterns = [

    # ==== token generating section ====
    path('admin/login/',ObtainAuthToken.as_view()),

    # ==== exam list create section ====
    path('add/',ExamListCreate.as_view()),

    
]