from django.db import models

# Create your models here.
class Thread(models.Model):
    conversationId = models.IntegerField(null=False)
    thread_author = models.CharField(max_length=150)
    thread_author_pp = models.ImageField(upload_to='img/pp')
    thread_tweets = models.CharField(max_length=2000)
    thread_time = models.DateTimeField()
