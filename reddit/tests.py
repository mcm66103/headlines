from django.test import TestCase

from .models import RedditPost
from .views_helper import scrape_reddit, get_page_content, get_keywords_from_content
from .models import RedditPost, Keyword

# Create your tests here.
class RedditTestCase(TestCase):
    def test_scraper(self):
        scrape_reddit("msp")
