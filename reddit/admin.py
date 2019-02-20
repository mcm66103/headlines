from django.contrib import admin
from .models import RedditPost, Keyword
# Register your models here.
admin.site.register(RedditPost)
admin.site.register(Keyword)