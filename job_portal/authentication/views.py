from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

def register(request):
    """
    get: 
    Return registration form if not already logged in else company view.

    post:
    Create new user instance do login and redirect to company view.
    """
    if request.user.is_authenticated:
        return redirect('company-view') 
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect("create-company")
    else:
        user_form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': user_form})
