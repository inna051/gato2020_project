from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from gato2020.profiles.forms import UserRegistrationForm

class UserHomeView(View):
    def get(self, request):
        context = {
            'title': 'Начална страница',
            'content': 'Това е началната страница на профилите.',
        }
        return render(request, 'profiles/home.html', context)
class UserLoginView(FormView):
    template_name = 'profiles/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class UserRegisterView(FormView):
    template_name = 'profiles/register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class UserProfileView(View):
    def get(self, request):
        return render(request, 'profiles/profile.html')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')