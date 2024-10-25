from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from TastyRecipes.profiles.models import Profile
from TastyRecipes.recipes.forms import CreateRecipeForm, UpdateRecipeForm, DeleteRecipeForm
from TastyRecipes.recipes.models import Recipe


# Create your views here.
class ListRecipeView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('recipe catalogue')
    form_class = CreateRecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

    def form_valid(self,form):
        form.instance.author = Profile.objects.first()
        return super().form_valid(form)


class DetailRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    pk_url_kwarg = 'recipe_id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        recipe = self.get_object()
        context['ingredients_list'] = recipe.ingredients.split(', ')
        return context



class UpdateRecipeView(UpdateView):
    model=Recipe
    template_name = 'recipes/edit-recipe.html'
    success_url = reverse_lazy('recipe catalogue')
    pk_url_kwarg = 'recipe_id'
    form_class = UpdateRecipeForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'recipes/delete-recipe.html'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('recipe catalogue')
    form_class = DeleteRecipeForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['form'] = self.form_class(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())