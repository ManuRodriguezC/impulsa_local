from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import CustomUser
from .forms import RegisterForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        form.get_user()
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save(commit=False)

        is_entrepreneur = form.cleaned_data.get('is_entrepreneur')
        if is_entrepreneur:
            user.role = 'emprendedor'
        else:
            user.role = 'usuario'

        user.save()

        login(self.request, user)

        return super().form_valid(form)