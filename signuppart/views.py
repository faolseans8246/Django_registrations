from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login

# Create your views here.

def webPage(request):
    return HttpResponse("Django loyiha ishga tushirildi!")

def signUpFunc(request):

    if request.method == "POST":
        form = SignUpForms(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("home")

    else:
        form = SignUpForms()

    return render(request, 'signup.html', {'form': form})

