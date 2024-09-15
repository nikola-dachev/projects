from . import views
from django.urls import path, include

from .views import AddAlbumView, DetailsAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = [
    path('add/', AddAlbumView.as_view(), name='add album'),
    path('<int:pk>/', include([
        path('details/', DetailsAlbumView.as_view(), name = 'details album'),
        path('edit/', EditAlbumView.as_view(), name = 'edit album'),
        path('delete/', DeleteAlbumView.as_view() , name = 'delete album')
    ]))
]