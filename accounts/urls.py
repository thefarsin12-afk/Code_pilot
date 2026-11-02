from django.urls import path

from accounts.views import AdminCreateViwe
from accounts.views import StudentCreateView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    #==== admin register section ====
    path("admin/register/",AdminCreateViwe.as_view()),

    #==== student registration ====
    path("student/register/",StudentCreateView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    # jwt token
    path('jwt/token/',TokenObtainPairView.as_view()),
    path('jwt/token/refresh/',TokenRefreshView.as_view())
]