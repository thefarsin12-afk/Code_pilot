from django.urls import path

from evaluation.views import SubmissionStartView,SubmissionListing
from evaluation.views import AnswerCreateView

urlpatterns = [

   path('assesment/<int:pk>/submission/',SubmissionStartView.as_view()),

   path('submission/all/',SubmissionListing.as_view()),

   path ('submission/<int:pk>/answer/',AnswerCreateView.as_view()),

]