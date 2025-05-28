from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")

class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()

class CustomPasswordResetForm(PasswordResetForm):
    captcha = CaptchaField()
