from django.urls import path
from .views import CreateComment, ListComment, CommentDetail


urlpatterns = [
    path("comment/<int:pk>/", CreateComment.as_view(),name='comment'),
    path("view_comments/<int:pk>/", ListComment.as_view(), name='comments'),
    path("comment/detail/<int:pk>/", CommentDetail.as_view(), name='comment_detail'),
]

