from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from exams.views import ExamListCreate
from exams.views import ExamRetrieveUpdateDelete


urlpatterns = [

    # ==== token generating section ====
    path('admin/login/',ObtainAuthToken.as_view()),

    # ==== exam list create section ====
    path('assessment/',ExamListCreate.as_view()),

    # ==== exam retrieve update delete section ====
    path('assessment/<int:pk>/',ExamRetrieveUpdateDelete.as_view()),

    
]