from rest_framework.generics import CreateAPIView, DestroyAPIView
from .serializer import ConnectionSerializer
from .models import Connection
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class Follow(CreateAPIView):
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated]

    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        target_user_id = self.kwargs.get("pk")
        
        target_user = get_object_or_404(User, pk =target_user_id)
        
        if user == target_user:
            return Response({"message": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        if Connection.objects.filter(follower=user, following=target_user).exists():
            return Response({"message": "You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)
        connection = Connection.objects.create(follower=user, following=target_user)
        serializer = self.serializer_class(connection)
        
        
        response = {
            "message": "Followed successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
        
class Unfollow(DestroyAPIView):
    permission_classes = [IsAuthenticated]


    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        target_user_id = self.kwargs.get('pk')
        target_user = get_object_or_404(User, pk=target_user_id)
        
        if user == target_user:
            return Response({"message": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        connection = get_object_or_404(Connection, follower=user, following=target_user)
        connection.delete()
        
        response = {
            "message": "Unfollowed successfully",
        }
        
        return Response(response, status=status.HTTP_200_OK)
