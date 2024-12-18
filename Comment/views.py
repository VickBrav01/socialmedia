from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from Post.models import Post
from .models import Comment


class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, pk=post_id)
        comment = serializer.save(author=user, post=post)
        return comment
    
class ListComment(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_queryset(self):
        post = self.kwargs.get("pk")
        comment = Comment.objects.filter(post = post)
        return comment
        
class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]
    
    
    # def get_queryset(self):
    #     post = self.kwargs.get("pk")
    #     comment = Comment.objects.filter(post = post)
    #     return comment
    


