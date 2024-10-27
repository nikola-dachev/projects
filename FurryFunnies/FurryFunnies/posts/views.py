from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.authors.models import Author
from FurryFunnies.posts.forms import CreatePostForm, UpdatePostForm, DeletePostForm
from FurryFunnies.posts.models import Post


# Create your views here.


class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = CreatePostForm


    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        return context



class DetailPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        return context


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'post_id'
    form_class = UpdatePostForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')
    form_class = DeletePostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.first()
        context['form'] = self.form_class(instance= self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())



