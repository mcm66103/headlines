import praw
from secrets import CLIENT_ID, CLIENT_SECRET

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent='desktop:myredditapp:v0.0.1 (by /u/clamchowderpowder)',)

print(reddit.read_only)  # Output: False


for submission in reddit.subreddit('msp').new(limit=100):
    print(submission.title)

