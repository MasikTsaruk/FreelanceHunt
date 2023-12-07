from django.urls import path
from . import views

urlpatterns = [
    path('', views.unfiltred, name='unfiltred'),
    path('filtred/<int:page>/', views.filtred, name='filtred')
]
