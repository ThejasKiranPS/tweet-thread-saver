from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from requests.api import request
from twitter_scripts import thread_fetch, profile_fetch
from .models import DeletedThread, Thread
from .forms import ConvoForm
    
# Create your views here.
def dashboard(request):
    if request.user.username == '':
        return redirect('/user_login')
    else:
        print(request.user.username + " Logged in")
        threads = Thread.objects.filter(user=request.user)
        return render(request=request, template_name="dashboard.html", context={'threads': threads, "username":request.user.username })


def refresh(request):
    print(f"refresh called by {request.user.username}")
    threads=thread_fetch.main(request.user.username)
    for thread in threads:
        convId = thread['conversation_id']
        author = thread['thread_author']
        author_username = thread['thread_author_username']
        tweets = thread['thread_tweets']
        twitter_thread=""
        profile_banner = profile_fetch.get_profile_url(author_username)
        for tweet in tweets:
            twitter_thread = twitter_thread +" "+ tweet
        new_thread = Thread(
            user=request.user,
            conversationId=convId,
            thread_author=author,
            thread_author_username=author_username,
            thread_author_banner=profile_banner,
            thread_tweets=twitter_thread
            )
        if not Thread.objects.filter(conversationId=convId,user=request.user).exists():
            if  not DeletedThread.objects.filter(conversationId=convId,user=request.user).exists():
                new_thread.save()

    return redirect("/dashboard")


def noLogin(request):

    return render(request=request, template_name='login.html')

def about(request):

    return render(request=request, template_name="about.html")

def addbyurl(response):
    
    if response.method == "POST":
        convId=response.POST['convoId']
    threads=thread_fetch.addByUrl(convId)
    for thread in threads:
        convId = thread['conversation_id']
        author = thread['thread_author']
        author_username = thread['thread_author_username']
        tweets = thread['thread_tweets']
        twitter_thread=""
        profile_banner = profile_fetch.get_profile_url(author_username)
        for tweet in tweets:
            twitter_thread = twitter_thread +" "+ tweet
        new_thread = Thread(
            user=response.user,
            conversationId=convId,
            thread_author=author,
            thread_author_username=author_username,
            thread_author_banner=profile_banner,
            thread_tweets=twitter_thread
            )
        if not Thread.objects.filter(conversationId=convId,user=request.user).exists():   
            new_thread.save()

    return redirect("/dashboard")

def deletethread(response):
    
    if response.method == "POST":
        convId = response.POST['convoId']
    thread = Thread.objects.get(conversationId=convId,user=response.user)
    deletedThread = DeletedThread(user=response.user,conversationId=thread.conversationId)
    deletedThread.save()
    thread.delete()

    return redirect("/dashboard")