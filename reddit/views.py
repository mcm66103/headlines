from datetime import timedelta, datetime
from .views_helper import get_top_keywords
from django.shortcuts import render, redirect
from .models import RedditPost
from .views_helper import (
    get_submissions, save_submissions, generate_keywords_from_post, get_keywords_by_keyword_and_subreddit,
    calc_keyword_percent_change
)

time_frame_options = {
    "day": timedelta(days=1),
    'week': timedelta(days=7),
    "month": timedelta(days=30),
    "year": timedelta(days=365),
}

# Create your views here.
def dashboard(request, subreddit):
    context = {}
    context['subreddit'] = subreddit
    limit = request.GET.get('limit', 100)
    time_frame = request.GET.get('time', 'week')

    context['top_keywords'] = get_top_keywords(time_frame_options[time_frame], subreddit, limit)
    last_periods_top_keywords = get_top_keywords(time_frame_options[time_frame], subreddit, limit,
                                                 start_time=datetime.now()-time_frame_options[time_frame])

    context['chart_data'] = calc_keyword_percent_change(context['top_keywords'], last_periods_top_keywords)
    return render(request, 'reddit/dashboard.html', context)

def add_keywords(request, subreddit):
    limit = int(request.GET.get('limit', 50))
    submissions = get_submissions(subreddit, limit)
    save_submissions(submissions)
    get_all_posts_without_keywords = RedditPost.objects.all().filter(keywords_generated=False)
    for submission in get_all_posts_without_keywords:
        print('generating keywords from submission: %s' % submission.title)
        generate_keywords_from_post(submission)
    return redirect('/%s/' % subreddit)



def keyword_detail(request, subreddit, keyword):
    context = {}
    time_frame = request.GET.get('time', 'week')
    context['keyword'] = keyword
    context['keyword_instances'] = get_keywords_by_keyword_and_subreddit(time_frame_options[time_frame], keyword, subreddit)
    return render(request, 'reddit/keyword-detail.html', context)

def home(request):
    return render(request, 'reddit/home.html')
