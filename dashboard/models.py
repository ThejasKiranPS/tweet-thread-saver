from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversationId = models.IntegerField(null=False)
    thread_author = models.CharField(max_length=150)
    thread_author_pp = models.ImageField(upload_to='img/pp')
    thread_tweets = models.CharField(max_length=2000)
    thread_time = models.DateTimeField()

    def __str__(self):
        return self.conversationId