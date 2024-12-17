from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Post
        fields = ["id", "author", "content", "image", "created_at",'updated_at']
        
    