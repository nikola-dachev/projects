from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.authors.forms import CreateAuthorForm, UpdateAuthorForm
from FurryFunnies.authors.models import Author


# Create your views here.


class CreateAuthorView(CreateView):
    model = Author
    template_name = 'authors/create-author.html'
    form_class = CreateAuthorForm
    success_url = reverse_lazy('dashboard')


class DetailAuthorView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_object(self,queryset=None):
        return Author.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        total_number_published_posts = Author.objects.first().posts.count() if Author.objects.first().posts else 0
        context['total_number_published_posts'] = total_number_published_posts
        last_updated_post = Author.objects.first().posts.order_by('-updated_at').first()
        context['last_updated_post'] = last_updated_post
        return context



class EditAuthorView(UpdateView):
    model = Author
    template_name = 'authors/edit-author.html'
    form_class = UpdateAuthorForm
    success_url = reverse_lazy('details author')

    def get_object(self,queryset=None):
        return Author.objects.first()


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self,queryset=None):
        return Author.objects.first()