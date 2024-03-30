from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from gato2020.profiles.forms import UserRegistrationForm

def home(request):
    context = {
        'title': 'Начална страница',
        'content': 'Това е началната страница на профилите.',
    }
    return render(request, 'profiles/home.html', context)

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        login_form = AuthenticationForm()

    return render(request, 'profiles/login.html', {'login_form': login_form})

class UserRegisterView(FormView):
    template_name = 'profiles/register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

def profile_view(request):
    return render(request, 'profiles/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')