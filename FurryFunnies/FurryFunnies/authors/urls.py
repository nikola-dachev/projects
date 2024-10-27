from django.urls import path,include

from FurryFunnies.authors import views
from FurryFunnies.authors.views import CreateAuthorView, DetailAuthorView,EditAuthorView,DeleteAuthorView

urlpatterns =[
    path('create/', CreateAuthorView.as_view(), name = 'create author'),
    path('details/', DetailAuthorView.as_view(), name='details author'),
    path('edit/', EditAuthorView.as_view(), name = 'edit author'),
    path('delete/', DeleteAuthorView.as_view(), name = 'delete author'),
]