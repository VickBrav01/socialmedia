
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("User.urls")),
    path("api/", include("Post.urls")),
    path("api/", include("Comment.urls")),
    path("api/", include("Follow.urls")),
    path("api/", include("Like.urls")),
    path("api/", include("Feed.urls")),
]
