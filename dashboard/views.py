from django.shortcuts import redirect, render
from twitter_scripts import thread_fetch

# Create your views here.
def dashboard(request):
    return render(request=request, template_name="dashboard.html")


def refresh(request):
    thread_fetch.main("thejaskiranps")

    return redirect('/dashboard')