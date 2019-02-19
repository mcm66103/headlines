import praw
from .secrets import CLIENT_ID, CLIENT_SECRET
from .models import RedditPost

def scrape_reddit(subreddit):
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent='desktop:myredditapp:v0.0.1 (by /u/clamchowderpowder)',)

    print(reddit.read_only)  # Output: False


    for submission in reddit.subreddit(subreddit).new(limit=100):

        # Check database for matching submission
        matching_submission = match_submission_by_id(submission)

        if not matching_submission:
            # Create a new one if there is no matching submission
            save_new_submission(submission)
        else:
            # Otherwise, update the match
            update_submission_score(matching_submission, submission)


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
