from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.

class UserManager(UserManager):
    
    def create_user(self, email, password=None, **extra_fields):
                
        if not email:
            raise ValueError("Enter a valid email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, null=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True, null=True)
    
    
    
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()
    
    
    
    def __str__(self):
        return self.username
    
    ...
