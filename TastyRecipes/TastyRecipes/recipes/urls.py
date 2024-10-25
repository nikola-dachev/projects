
from django.urls import path,include

from TastyRecipes.recipes import views
from TastyRecipes.recipes.views import CreateRecipeView, ListRecipeView, DetailRecipeView, UpdateRecipeView, \
    DeleteRecipeView

urlpatterns = [
    path('catalogue/', ListRecipeView.as_view(), name = 'recipe catalogue'),
    path('create/', CreateRecipeView.as_view(), name = 'create recipe'),
    path('<int:recipe_id>/', include([
        path('details/', DetailRecipeView.as_view(), name = 'recipe details'),
        path('edit/', UpdateRecipeView.as_view(), name = 'edit recipe'),
        path('delete/',DeleteRecipeView.as_view(), name = 'delete recipe'),
    ]))
]