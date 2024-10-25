from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from WorldOfSpeed.cars.forms import CreateCarForm, UpdateCarForm, DeleteCarForm
from WorldOfSpeed.cars.models import Car
from WorldOfSpeed.profiles.models import Profile


# Create your views here.
def catalogue_car(request):
    pass

class ListCarView(ListView):
    model = Car
    template_name = 'cars/catalogue.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['total_cars'] = Car.objects.count()
        return context


class CreateCarView(CreateView):
    model = Car
    template_name = 'cars/car-create.html'
    form_class =CreateCarForm
    success_url = reverse_lazy('catalogue car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form = form)


class DetailCarView(DetailView):
    model=Car
    template_name = 'cars/car-details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class EditCarView(UpdateView):
    model= Car
    template_name ='cars/car-edit.html'
    pk_url_kwarg = 'id'
    form_class =UpdateCarForm
    success_url = reverse_lazy('catalogue car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    pk_url_kwarg = 'id'
    form_class = DeleteCarForm
    success_url = reverse_lazy('catalogue car')

    def get_context_data(self, **kwargs):
        car = self.get_object()
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['form'] = self.form_class(instance=car)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

