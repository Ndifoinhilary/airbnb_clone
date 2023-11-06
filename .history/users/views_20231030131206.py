from django.shortcuts import render
from django.views import View 

from .forms import LoginForm


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
        context ={
            'form':form
        }
        return render(request, 'users/login', context)

