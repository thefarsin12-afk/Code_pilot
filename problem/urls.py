from django.urls import path
from problem.views import QuestionCreateView
from problem.views import QuestionRetrieveUpdateDeleteView

urlpatterns = [

    # create qustion route
    path('assesment/<int:pk>/question/',QuestionCreateView.as_view()),

    # 
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),



] 