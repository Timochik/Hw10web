from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from .models import Author, Quote

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']