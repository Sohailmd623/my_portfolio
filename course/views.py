from django.shortcuts import render, get_object_or_404

from .models import Course
# Create your views here.

def allcourse(request):
    courses = Course.objects
    return render(request, "course/allcourse.html", {"courses": courses})
