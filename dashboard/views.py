from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request=request, template_name="dashboard.html")