from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            self.add_error("password", forms.ValidationError(
                "Password not correct"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError(
                "User does not exits"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name','last_name','email']
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    password1 = forms.CharField(
        widget=forms.PasswordInput, label='comfim password')


    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit= False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user.username = email
        user.set_password(password)
        user.save()
        return user