from djongo import models
from django.contrib.auth.models import AbstractUser


PROFILE_CHOICES = (
    (1, 'Super Admin'),
    (2, 'Admin'),
    (3, 'Manager'),
    (4, 'Client'),
    (5, 'Expert'),
)

class User(AbstractUser):
    
    user_type = models.IntegerField(choices=PROFILE_CHOICES)
    
    def __str__(self):
        return self.username
    
    
