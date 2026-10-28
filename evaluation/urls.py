from django.urls import path

from evaluation.views import SubmissionStartView

urlpatterns = [

   path('assesment/<int:pk>/submission/',SubmissionStartView.as_view()),

]