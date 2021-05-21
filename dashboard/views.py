from django.shortcuts import redirect, render
from twitter_scripts import thread_fetch
from .models import Thread

# Create your views here.
def dashboard(request):
    
    current_user = request.user.id
    threads = Thread.objects.filter(username=current_user)
    return render(request=request, template_name="dashboard.html", context={'threads': threads})


def refresh(request):
    
    # this is where we will run the script to add new mentions to our database 
    # and store them


    return redirect('/dashboard')