from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializer import PostSerializer
from .models import Post


    

# The `PostCreateView` class is a Django REST framework view for creating posts with the authenticated
# user as the author.
class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(author=user)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    
# The `PostListView` class is a Django REST framework view that lists posts authored by the
# authenticated user.
class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(author=user)
        return post

    
# This class defines views for retrieving, updating, and deleting a Post object with authentication
# checks based on the requesting user's ID.
class PostDetailView(views.APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        post = Post.objects.filter(pk=pk)
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        post = Post.objects.filter(pk=pk)
        data = self.request.data
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=post, data=data, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        post = Post.objects.filter(pk=pk)
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_200_OK)
   