from . import views
from django.urls import path

from .views import DetailsProfileView, DeleteProfileView

urlpatterns = [
    path('details/', DetailsProfileView.as_view(), name='details profile'),
    path('delete/', DeleteProfileView.as_view(), name = 'delete profile')
]