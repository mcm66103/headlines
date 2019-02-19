from django.db import models
# Create your models here.
class Keyword(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word


class RedditPost(models.Model):
    title = models.CharField(max_length=255)
    score = models.IntegerField()
    id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField()
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.title
