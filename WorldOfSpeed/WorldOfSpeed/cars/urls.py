from django.urls import path,include

from WorldOfSpeed.cars import views
from WorldOfSpeed.cars.views import CreateCarView, ListCarView, DetailCarView, EditCarView, DeleteCarView

urlpatterns = [
    path('catalogue/', ListCarView.as_view(), name='catalogue car'),
    path('create/', CreateCarView.as_view(), name = 'create car'),
    path('<int:id>/', include([
        path('details/', DetailCarView.as_view(), name = 'car details'),
        path('edit/', EditCarView.as_view(), name = 'car edit'),
        path('delete/', DeleteCarView.as_view(), name = 'car delete'),
    ]))
]