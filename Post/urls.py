from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    path("post/", PostCreateView.as_view(), name='posts'),
    path("post/<int:pk>/", PostListView.as_view(), name='posts'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name="post_detail")
]
