from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import FeedSerializer
from Post.models import Post
from django.db.models import Q
from django.contrib.auth import get_user_model
from Follow.models import Connection


User = get_user_model()
# The `Feeds` class retrieves posts authored by the current user or users they follow.

class Feeds(ListAPIView):
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    
    def get_queryset(self):
        user = self.request.user 
        target_user = Connection.objects.filter(follower=user).values_list("following", flat=True)
        post = Post.objects.filter(Q(author=user) | Q(author__in=target_user))
        return post
    
    