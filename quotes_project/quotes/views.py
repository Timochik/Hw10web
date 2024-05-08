from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .forms import QuoteForm
from .forms import AuthorForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # User is authenticated, redirect to desired page
            return redirect('/')  # Redirect to homepage after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required  # This decorator requires user login
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_authors')  # Redirect to a list of authors after successful creation
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_quotes')  # Redirect to a list of quotes after successful creation
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})

