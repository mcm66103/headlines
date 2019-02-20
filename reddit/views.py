from datetime import timedelta
from .views_helper import get_top_keywords
from django.shortcuts import render

# Create your views here.
def dashboard(request, subreddit):
    context = {}
    time_frame_options = {
        "day": timedelta(days=1),
        "week": timedelta(days=7),
        "month": timedelta(days=30),
        "year": timedelta(days=365),
    }

    limit = request.GET.get('limit', 100)
    time_frame = request.GET.get('time', 'week')

    context['top_keywords'] = get_top_keywords(time_frame_options[time_frame], subreddit, limit)



def keyword_detail(request):
    pass

def home(request):
    return render(request, 'reddit/home.html')
