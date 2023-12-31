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


class SignupForm(forms.Form):
    pass