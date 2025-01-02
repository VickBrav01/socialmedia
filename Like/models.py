from django.db import models
from django.contrib.auth import get_user_model
from Post.models import Post

User =get_user_model()
# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user} likes {self.post}"