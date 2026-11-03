from django.urls import path

from accounts.views import AdminCreateViwe
from accounts.views import StudentCreateView
from accounts.views import ProfileUpdateView
from accounts.views import GetMeView

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

    path('jwt/token/refresh/',TokenRefreshView.as_view()),

    path('profile/complted/',ProfileUpdateView.as_view()),

    path('me/',GetMeView.as_view()),
]