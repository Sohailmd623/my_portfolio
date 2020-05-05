from django.shortcuts import render

from .models import Acad

def allacad(request):
    acads = Acad.objects
    return render(request, "acad/allacad.html", {"acads": acads})
