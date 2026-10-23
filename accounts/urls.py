from django.urls import path

from accounts.views import AdminCreateViwe
from accounts.views import StudentCreateView

urlpatterns = [

    #==== admin register section ====
    path("admin/register/",AdminCreateViwe.as_view()),

    #==== student registration ====
    path("student/register/",StudentCreateView.as_view()),
]