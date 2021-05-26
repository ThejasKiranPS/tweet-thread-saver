from loginapp import urls
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from twitter_scripts import profile_fetch


def home(request):
    return render(request=request, template_name="homepage.html")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if not profile_fetch.get_profile(response.POST['username']):
            # form = RegisterForm(response.POST)
            error_message = [
                f"Twitter username {response.POST['username']} doesn't exist"]
            error_message.append("Please user your existing twiter ID")
            print(error_message)
            return render(response, 'register.html', {'error_message': error_message})

        else:
            if form.is_valid():
                error_message = [
                    f"Twitter {response.POST['username']} doesn't exist"]
                form.save()
                return redirect("/dashboard")

            else:
                form = RegisterForm()
                print("No Response")

    return render(response, "register.html")


def logout(response):
    render("logout.html")
