from rest_framework import serializers
from .models import Post
from Comment.serializer import CommentSerializer
from Like.serializer import LikeSerializer



# The `PostSerializer` class serializes Post objects with fields for author, content, image, comments,
# likes, created_at, and updated_at.
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Post
        fields = ["id", "author", "content", "image", "comments","likes", "created_at",'updated_at']
        
    