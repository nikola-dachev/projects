from django.shortcuts import render

from TastyRecipes.profiles.models import Profile


# Create your views here.

def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }

    return render(request, 'common/home-page.html', context)