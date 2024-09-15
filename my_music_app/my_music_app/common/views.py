from django.shortcuts import render, redirect

from my_music_app.albums.models import Album
from my_music_app.profiles.forms import CreateProfileForm
from my_music_app.profiles.models import Profile


# Create your views here.
def index(request):
    user = Profile.objects.first()
    albums = Album.objects.all()

    context = {
        'user': user,
        'albums': albums
    }

    if user:
        return render(request, 'common/home-with-profile.html', context)

    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('index')

    context['form'] = form
    return render(request, 'common/home-no-profile.html',context)