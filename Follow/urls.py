from django.urls import path
from .views import Follow, Unfollow

urlpatterns = [
    path('follow/<int:pk>/', Follow.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', Unfollow.as_view(), name='unfollow_user'),
]