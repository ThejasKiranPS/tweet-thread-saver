from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    conversationId = models.IntegerField(null=False)
    thread_author = models.CharField(max_length=150)
    thread_author_username = models.CharField(max_length=150)
    thread_tweets = models.CharField(max_length=2000)

    def __str__(self):
        return self.conversationId
