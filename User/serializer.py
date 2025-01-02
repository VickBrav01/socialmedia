# from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(read_only=True)
    profile_picture = serializers.ImageField(read_only=True)
    class Meta:
        model = User
        fields = ["id","username", "email", "password", "bio", "profile_picture"]
        
    def create(self, validated_data):
    
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data['email'],
            password=validated_data['password'],
           
        )
        
        return user