from django.shortcuts import render
from .models import Competition
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    competition_linkcarrer = Competition.objects.filter(platform='linkcarrer').order_by('-id')[:10]
    competition_wevity = Competition.objects.filter(platform='wevity').order_by('-id')[:10]
    competition_thinkgood = Competition.objects.filter(platform='thinkgood').order_by('-id')[:10]

    context = {
        'competition_linkcarrer': competition_linkcarrer,
        'competition_wevity': competition_wevity,
        'competition_thinkgood': competition_thinkgood
    }
    return render(request, 'mainpage/index.html', context)

def search(request):
    keyword = request.GET.get('q')
    searched_competitions = Competition.objects.filter(title__icontains=keyword)

    paginator = Paginator(searched_competitions, 10)  # 페이지 당 10개의 결과를 보여줌
    page_number = request.GET.get('page')

    try:
        searched_competitions = paginator.page(page_number)
    except PageNotAnInteger:
        searched_competitions = paginator.page(1)
    except EmptyPage:
        searched_competitions = paginator.page(paginator.num_pages)
    
    context = {
        'keyword': keyword,
        'competitions': searched_competitions
    }
    return render(request, 'mainpage/search.html', context)