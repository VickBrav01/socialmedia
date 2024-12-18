from rest_framework import serializers
from .models import Post
from Comment.serializer import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Post
        fields = ["id", "author", "content", "image", "comments", "created_at",'updated_at']
        
    