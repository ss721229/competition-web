from django.shortcuts import render
from .models import Competition

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