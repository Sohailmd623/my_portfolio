from django.shortcuts import render

# Create your views here

from .models import Job

def home(request):
     jobs = Job.objects
     return render(request, "home.html", {"jobs":jobs})