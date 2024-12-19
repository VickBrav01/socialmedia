from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(read_only=True)
    profile_picture = serializers.ImageField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "followers", "following", "profile_picture"]
    def get_followers(self, obj):
        
        return obj.followers.values_list('follower_id', flat=True)

    def get_following(self, obj):
        
        return obj.following.values_list('following_id', flat=True)
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        return user