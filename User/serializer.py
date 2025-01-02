from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

# The `UserSerializer` class serializes user data including followers and following relationships,
# with methods to retrieve followers and following lists and create a new user instance.
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
        
        return obj.followers.values_list('follower', flat=True)

    def get_following(self, obj):
        
        return obj.following.values_list('following', flat=True)
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        return user