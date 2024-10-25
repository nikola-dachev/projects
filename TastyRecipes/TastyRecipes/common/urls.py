from django.urls import path,include

from TastyRecipes.common import views

urlpatterns = [
    path('', views.index, name='index'),
]