from django.test import TestCase
from time import sleep
from datetime import timedelta

from .models import RedditPost

from .views_helper import get_submissions, save_submissions, generate_keywords_from_post, get_top_keywords


def get_100_subreddit_msp_submissions():
    return get_submissions("msp", 100)


# Create your tests here.
class RedditTestCase(TestCase):
    def test_scraper(self):
        new_submissions = get_100_subreddit_msp_submissions()
        i = 1
        while i < 20:
            for submission in new_submissions:
                print("submission.title: %s" % submission.title)
                self.assertIsInstance(submission.title, str)
                i += 1
        sleep(3)

    def test_save_scraper_data(self):

        new_submissions = get_100_subreddit_msp_submissions()
        save_submissions(new_submissions)
        self.assertTrue(RedditPost.objects.all().count() == 100)

    def test_generate_keywords_from_scraper_data(self):
        new_submissions = get_100_subreddit_msp_submissions()
        save_submissions(new_submissions)
        reddit_posts = RedditPost.objects.all()
        i = 0
        while i < 1:
            for post in reddit_posts:
                if post.keywords_generated == False:
                    generate_keywords_from_post(post)
                    test_post = RedditPost.objects.get(id=post.id)
                    print(test_post.keywords_generated)
                    sleep(2)
                    self.assertTrue(test_post.keywords_generated)
                break
            break
        self.assertFalse(reddit_posts[i+1].keywords_generated)

class DashboardTestCase(TestCase):
    def setUp(self):
        new_submissions = get_100_subreddit_msp_submissions()
        save_submissions(new_submissions)
        reddit_posts = RedditPost.objects.all()
        for post in reddit_posts:
            if post.keywords_generated == False:
                generate_keywords_from_post(post)
                test_post = RedditPost.objects.get(id=post.id)
                print(test_post.keywords_generated)
                sleep(.2)

    def test_get_top_keywords(self):
        mytimedelta = timedelta(days=7)
        limit = 100
        subreddit = "msp"
        top_keywords = get_top_keywords(mytimedelta, subreddit, limit)
        self.assertEqual(len(top_keywords), limit)
