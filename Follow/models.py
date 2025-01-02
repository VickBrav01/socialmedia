from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Connection(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models  .CASCADE, default=None)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, default=None)
    
    class Meta:
        unique_together = ("follower", "following")
        
    def __str__(self):
        return f"{self.follower} follows {self.following}"
