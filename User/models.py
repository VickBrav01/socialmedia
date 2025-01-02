from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.

class UserManager(UserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """
        The function creates a user with an email, password, and additional fields.
        
        :param email: The `create_user` method you provided is a common pattern used in Django for
        creating user objects. It takes in several parameters:
        :param password: The `create_user` method you provided is a common pattern used in Django for
        creating user objects. The `create_user` method takes in several parameters:
        :return: The `create_user` method returns the user object that has been created and saved in the
        database.
        """
        
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
