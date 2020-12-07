from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects})

def media(request):

    full_url = request.build_absolute_uri
    return render(request, 'portfolio/media.html',
        {'full_url':full_url})
