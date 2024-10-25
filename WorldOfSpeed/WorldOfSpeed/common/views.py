from django.shortcuts import render

from WorldOfSpeed.profiles.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)