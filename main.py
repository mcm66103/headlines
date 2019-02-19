import praw


reddit = praw.Reddit(client_id='U3c5VG-B0wgeEA',
                     client_secret='ZxjowE_k5Nsi8CT617Ze-uYL0EE',
                     user_agent='desktop:myredditapp:v0.0.1 (by /u/clamchowderpowder)',)

print(reddit.read_only)  # Output: False


for submission in reddit.subreddit('msp').new(limit=100):
    print(submission.title)

