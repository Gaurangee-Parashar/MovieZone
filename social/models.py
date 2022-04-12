from email import contentmanager
from email.policy import default
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    id = models.UUIDField(primary_key=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(self):
        return ChatMessage.objects.order_by('-timestamp').all()[:10]