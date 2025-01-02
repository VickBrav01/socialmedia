from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializer import UserSerializer

User = get_user_model()




# The `Register` class is an API view in Python that handles user registration by validating user
# input, creating a new user, and generating access tokens.
class Register(APIView):
    serializer_class = UserSerializer
    
    
    def post(self,request:Request, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            response = {
                "message": "User Created",
                "data": serializer.data,
                
            }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# The class `Login` is a subclass of `TokenObtainPairView` in Python.
class Login(TokenObtainPairView):
    pass



# The `Profile` class in this Python code defines API views for retrieving, updating, and deleting
# user profiles with authentication checks.
class Profile(APIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    permission_classes= [IsAuthenticated]
    
    def get(self, request:Request, *args, **kwargs):
        
        pk = self.kwargs.get("pk")
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
            

        user = get_object_or_404(User,pk=pk)
        serializer = self.serializer_class(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def patch(self, request:Request, *args, **kwargs):
        
        pk = self.kwargs.get("pk")
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
            
        user = get_object_or_404(User,pk=pk)
        
        data = request.data
        
        serializer = self.serializer_class(instance=user, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message": "Profile Updated",
                "data": serializer.data
            }
            
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request:Request,*args, **kwargs):
        pk = self.kwargs.get("pk")
        if self.request.user.id != pk:
            return Response({"message": "User not authenticated"},status=status.HTTP_400_BAD_REQUEST)
            
        user = get_object_or_404(User,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
