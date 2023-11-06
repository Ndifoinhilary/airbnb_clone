from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm,SignUpForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(request, 'users/login.html',context)
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
            
        context ={
            'form':form
        }
        return render(request, 'users/login', context)

def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm 
    success_url = reverse_lazy('core:home')