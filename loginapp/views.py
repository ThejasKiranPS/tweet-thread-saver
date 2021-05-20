from django.http.response import HttpResponse
from django.shortcuts import  render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request=request, template_name="homepage.html")

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		
		return redirect("/dashboard")
	else:
		form = RegisterForm()
	return render(response,"register.html", {"form":form})
