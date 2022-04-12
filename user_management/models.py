from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.ImageField(default="default.png", null=True, blank=True, )

    def __str__(self):
        return str(self.user)
