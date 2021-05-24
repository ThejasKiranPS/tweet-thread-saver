from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversationId = models.IntegerField(null=False)
    thread_author = models.CharField(max_length=150)
    thread_author_username = models.CharField(max_length=150)
    thread_author_banner = models.CharField(max_length=100)
    thread_tweets = models.CharField(max_length=2000)


class DeletedThread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversationId = models.IntegerField(null=False)
