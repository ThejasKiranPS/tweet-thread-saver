from django.shortcuts import redirect, render
from twitter_scripts import thread_fetch
from .models import Thread

# Create your views here.
def dashboard(request):
    
    threads = Thread.objects.all()
    return render(request=request, template_name="dashboard.html", context={'threads': threads})


def refresh(request):
    thread_fetch.main("thejaskiranps")

    return redirect('/dashboard')