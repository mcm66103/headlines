from django.db import models

# Create your models here.
class RedditPost(models.Model):
    title = models.CharField(max_length=255)
    score = models.IntegerField()
    id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField()
