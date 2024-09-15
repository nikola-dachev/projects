from django.shortcuts import render
from django.views.generic import DetailView, DeleteView

from my_music_app.profiles.models import Profile


# Create your views here.


class DetailsProfileView(DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()


class DeleteProfileView(DeleteView):
    template_name = 'profiles/profile-delete.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()
