from django.urls import path
from . import views

urlpatterns = [
    path('important_clients/', views.important_clients_list, name='important_clients_list'),
    path('add_client/', views.add_client, name='add_client'),
]
