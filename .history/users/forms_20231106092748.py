from django import forms
from . import models

class LoginForm(forms.Form):
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user=models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            self.add_error("password",forms.ValidationError("Password not correct"))
        except models.User.DoesNotExist:
            self.add_error("email",forms.ValidationError("User does not exits"))


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label='comfim password')
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError('User with this email already exits')
        except models.User.DoesNotExist:
            return email
    
    
    
    def clean_password1(self):
        password = self.clean_data.get('password')
        password1 = self.clean_data.get('password1')
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password