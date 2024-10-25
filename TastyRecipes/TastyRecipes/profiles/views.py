from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from TastyRecipes.profiles.forms import CreateProfileForm, UpdateProfileForm
from TastyRecipes.profiles.models import Profile


# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    form_class =CreateProfileForm
    success_url = reverse_lazy('recipe catalogue')


class DetailProfileView(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_object(self,queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        profile= self.get_object()
        context['published_recipes']= profile.recipes.count()
        return context


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('profile details')
    form_class = UpdateProfileForm

    def get_object(self,queryset=None):
        return Profile.objects.first()


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.first()