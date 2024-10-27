from django.urls import path,include

from FurryFunnies.core import views
from FurryFunnies.core.views import ListDashboardView

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', ListDashboardView.as_view(), name = 'dashboard'),
]