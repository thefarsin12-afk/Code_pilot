from django.urls import path
from problem.views import QuestionCreateView

urlpatterns = [

    # create qustion route
    path('assesment/<int:pk>/question/',QuestionCreateView.as_view()),

] 