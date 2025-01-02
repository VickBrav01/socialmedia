from django.urls import path
from .views import Register, Login, Profile 

urlpatterns =[
    path("register/", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("profile/<int:pk>/", Profile.as_view(), name="profile")
]