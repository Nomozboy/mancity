from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


