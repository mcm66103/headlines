from django.db import models
# Create your models here.



class RedditPost(models.Model):
    title = models.CharField(max_length=255)
    score = models.IntegerField()
    id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField()
    keywords_generated = models.BooleanField(default=False)
    selftext = models.TextField()
    subreddit = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Keyword(models.Model):
    word = models.CharField(max_length=255)
    associated_post = models.ManyToManyField(RedditPost, related_name='associated_post')

    def __str__(self):
        return self.word
