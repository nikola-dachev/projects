from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeed.cars.models import Car
from WorldOfSpeed.profiles.forms import CreateProfileForm, UpdateProfileForm
from WorldOfSpeed.profiles.models import Profile


# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class =CreateProfileForm
    success_url = reverse_lazy('catalogue car')


class DetailProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        total_price = Car.objects.filter(owner =Profile.objects.first()).aggregate(Sum('price'))['price__sum']
        context['total_price'] = total_price if total_price is not None else 0.00
        return context



class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile details')
    form_class = UpdateProfileForm

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class DeleteProfileView(DeleteView):
    model= Profile
    template_name = 'profiles/profile-delete.html'
    success_url=reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.first()