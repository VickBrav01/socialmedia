from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["user", "post", "created_at"]
        

