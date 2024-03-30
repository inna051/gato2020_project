from django.urls import path
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('', views.home, name='profile_home'),
    path('login/', views.login_view, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
