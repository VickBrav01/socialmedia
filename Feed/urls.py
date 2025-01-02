from django.urls import path
from .views import Feeds

urlpatterns = [
    path("feeds/", Feeds.as_view(), name='feeds'),
]
