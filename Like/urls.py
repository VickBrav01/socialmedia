from django.urls import path
from .views import CreateLike, DeleteLike

urlpatterns = [
    path("like/<int:pk>/", CreateLike.as_view(), name="like"),
    path("unlike/<int:pk>/", DeleteLike.as_view(), name="unlike")
]
