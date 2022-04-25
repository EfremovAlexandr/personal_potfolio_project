from django.shortcuts import render
from .models import ProjectBlog


def home(request):
    projects = ProjectBlog.objects.all()
    return render(request, 'blog/home.html',)


def all_blogs(request):
    return render(request, 'blog/all_blogs.html')


