from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm,SignUpForm


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm 
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email= email , password = password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    

def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm 
    success_url = reverse_lazy('core:home')
    
    
    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email= email , password = password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)

def complete_vrification(self, key):
    pass