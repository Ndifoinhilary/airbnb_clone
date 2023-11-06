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
        context ={
            'form':form
        }
        return render(request, 'users/login', context)

