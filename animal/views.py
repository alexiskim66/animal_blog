from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Blog
from .forms import PostForm
from django.utils import timezone
from .models import Pictures ##


def home(request):
    objects = Blog.objects.all()
    return render(request, 'home.html', {'objects':objects})

def home_tn(request):
    blog = Pictures.objects ##
    return render(request, 'home.html', {'blog':blog})

def detail(request,content_id):
    blog = get_object_or_404(Blog, pk = content_id)
    return render(request, 'detail.html', {'blog':blog})



def delete(request,id):
    d_blog = Blog.objects.get(id=id)
    d_blog.delete()
    return redirect('home')

def animals(request):
    objects = Blog.objects.all()
    return render(request, 'animals.html', {'objects':objects})
    
def new(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        post_form = PostForm()
        return render(request, 'new.html', {'post_form':post_form})

def edit(request, id):
    post = get_object_or_404(Blog, pk=id)
    if request.method == 'GET':
        post_form = PostForm(instance=post)
        return render(request, 'edit.html', {'edit_Post':post_form})
    else:
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.date = timezone.now()
            post.save()
        return redirect('/animal/detail/' + str(id))
