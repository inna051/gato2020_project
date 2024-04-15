from django.urls import path
from .views import UserHomeView, UserRegisterView, UserLoginView, UserProfileView, UserLogoutView

urlpatterns = [
    path('', UserHomeView.as_view(), name='profile_home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]
