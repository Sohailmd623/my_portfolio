from django.shortcuts import render

from .models import Project

def allproject(request):
    projects = Project.objects
    return render(request, "project/allproject.html", {"projects": projects})