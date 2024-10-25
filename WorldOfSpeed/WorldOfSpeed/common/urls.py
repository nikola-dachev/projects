from django.urls import path,include

from WorldOfSpeed.common import views

urlpatterns = [
    path('', views.index, name='index'),
]