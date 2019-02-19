from django.test import TestCase

from .models import RedditPost
from .views_helper import scrape_reddit

# Create your tests here.
class RedditTestCase(TestCase):
    def test_scraper(self):
        scrape_reddit("msp")