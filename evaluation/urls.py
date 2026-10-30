from django.urls import path

from evaluation.views import SubmissionStartView,SubmissionListing,SubmissionRetrieveView
from evaluation.views import AnswerCreateView,AnswerUpdateView

urlpatterns = [

   # submission create
   path('assesment/<int:pk>/submission/',SubmissionStartView.as_view()),

   # submission list
   path('submission/all/',SubmissionListing.as_view()),

   # sumission retrieve
   path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),

   # answer create
   path ('submission/<int:pk>/answer/',AnswerCreateView.as_view()),

   # answer put 
   path('answer/<int:pk>/',AnswerUpdateView.as_view()),




]