from django.urls import path,include

from WorldOfSpeed.profiles import views
from WorldOfSpeed.profiles.views import CreateProfileView, DetailProfileView, UpdateProfileView,DeleteProfileView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('details/',DetailProfileView.as_view(), name= 'profile details'),
    path('update/', UpdateProfileView.as_view(), name = 'update profile'),
    path('delete/', views.DeleteProfileView.as_view() , name = 'delete profile'),
]