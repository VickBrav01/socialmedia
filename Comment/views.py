from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from Post.models import Post
from .models import Comment



# This class is used to create a comment associated with a specific post in a Django REST framework API.

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, pk=post_id)
        comment = serializer.save(author=user, post=post)
        return comment
    
    
# This class is a ListAPIView for Comment objects with authentication permission.
class ListComment(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        post = self.kwargs.get("pk")
        comment = Comment.objects.filter(post = post)
        return comment
    
    
        
# The `CommentDetail` class is a view for retrieving, updating, and deleting individual comment instances with authentication required.
class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    



