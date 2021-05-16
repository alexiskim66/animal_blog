from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Blog
from django.utils import timezone


def list(request):
    objects = Blog.objects.all()
    return render(request, 'list.html', {'objects':objects})

# Create your views here.
