from rest_framework.generics import CreateAPIView, DestroyAPIView
from .serializer import LikeSerializer
from .models import Like
from Post.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


# This class is responsible for creating a like for a post, checking if the user has already liked the
# post, and returning appropriate responses.
class CreateLike(CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")      
        user = self.request.user  
        post = get_object_or_404(Post, pk=pk)
        
        if Like.objects.filter(user=user, post=post).exists():
            return Response(
                {"message": "You already like the post"}, status=status.HTTP_208_ALREADY_REPORTED
            )
            
        
        like = Like.objects.create(user=user, post=post)
        serializer = self.serializer_class(like)
        
        response = {
            "messsage": "Liked",
            "data": serializer.data
        }
        return Response(response, status= status.HTTP_201_CREATED)
        
            
        
        
# This class defines a view for deleting a like on a post by a user.
    
class DeleteLike(DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs.get("pk")
        
        post = get_object_or_404(Post, pk=pk)
        
        like = get_object_or_404(Like, user=user, post=post)
        like.delete()
        response = {
            "message": "You have Unliked the post"
        }
        
        return Response(response, status=status.HTTP_200_OK)


        
