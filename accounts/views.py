from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
class SignupView(generic.CreateView):
    form_class= UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'

def logout_page(request):
	return redirect('index')