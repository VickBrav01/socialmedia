from rest_framework import serializers
from Post.models import Post
from Comment.serializer import CommentSerializer

class FeedSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = Post
        fields = ["author", "content", "image", "comments", "likes","created_at", "updated_at"]

    def get_likes(self, obj):
        return obj.likes.count()