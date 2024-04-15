from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('add/', views.add_city_view, name='add_city'),
]
