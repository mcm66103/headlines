import praw
import requests
from rake_nltk import Rake
from bs4 import BeautifulSoup


from .secrets import CLIENT_ID, CLIENT_SECRET
from .models import RedditPost, Keyword

def scrape_reddit(subreddit):
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent='desktop:myredditapp:v0.0.1 (by /u/clamchowderpowder)',)

    for submission in reddit.subreddit(subreddit).new(limit=100):

        # Check database for matching submission
        matching_submission = match_submission_by_id(submission)

        if not matching_submission:
            # Create a new one if there is no matching submission
            save_new_submission(submission)
            submission_keyword_list = get_keywords_from_content(get_page_content(submission.url))
            create_objects_from_high_value_keywords(submission, submission_keyword_list)

        else:
            # Otherwise, update the match
            update_submission_score(matching_submission, submission)


def get_page_content(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    headers = {'user-agent': user_agent}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup.stripped_strings

def get_keywords_from_content(content):
    r = Rake()
    r.extract_keywords_from_sentences(content)
    return r.get_ranked_phrases()


def create_objects_from_high_value_keywords(submission, keyword_list):
    for keyword in keyword_list:
        print(str(keyword))

def match_submission_by_id(submission):
    try:
        return RedditPost.objects.get(id = submission.id)
    except Exception:
        return False


def update_submission_score(matching_submission, submission):
    matching_submission.score = submission.score
    matching_submission.save()


def save_new_submission(submission):
    new_submission = RedditPost()
    new_submission.title = submission.title
    new_submission.id = submission.id
    new_submission.url = submission.url
    new_submission.score = submission.score
    new_submission.save()
