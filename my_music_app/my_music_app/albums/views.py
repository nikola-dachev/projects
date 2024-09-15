from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile


# Create your views here.

class GetFormMixin:
    def get_form(self, form_class=None):

        form = super().get_form(form_class=form_class)
        form.fields['album_name'].widget.attrs={'placeholder':'Album Name'}
        form.fields['artist_name'].widget.attrs={'placeholder':'Artist Name'}
        form.fields['description'].widget.attrs = {'placeholder':'Description'}
        form.fields['image_url'].widget.attrs = {'placeholder':'Image URL'}
        form.fields['price'].widget.attrs = {'placeholder':'Price'}
        return form

class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attr['readonly'] = 'readonly'
        return form


class AddAlbumView(GetFormMixin,CreateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')
    #
    # def get_form(self,form_class=None):
    #     form = super().get_form()
    #     form.fields['album_name'].widget.attrs={'placeholder':'Album Name'}
    #     form.fields['artist_name'].widget.attrs={'placeholder':'Artist Name'}
    #     form.fields['description'].widget.attrs = {'placeholder':'Description'}
    #     form.fields['image_url'].widget.attrs = {'placeholder':'Image URL'}
    #     form.fields['price'].widget.attrs = {'placeholder':'Price'}
    #     return form

    def form_valid(self,form):
        form.instance.owner_id = Profile.objects.first().pk
        return super().form_valid(form)


class DetailsAlbumView(DetailView):
    queryset = Album.objects.all()
    template_name = 'albums/album-details.html'


class EditAlbumView(GetFormMixin, UpdateView):
    queryset = Album.objects.all()
    template_name = 'albums/album-edit.html'
    fields = ('album_name', 'artist_name', 'genre', 'genre', 'description', 'image_url', 'price')
    success_url = reverse_lazy('index')




class DeleteAlbumView(DeleteView):
    queryset = Album.objects.all()
    template_name = 'albums/album-delete.html'
    success_url =reverse_lazy('index')
    form_class = modelform_factory(Album, fields=('album_name', 'artist_name', 'genre', 'genre', 'description', 'image_url', 'price'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs