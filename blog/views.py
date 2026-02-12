from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.published.all()[:6]
    context = {
        'title': 'Home Page',
        'posts': posts 
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def single(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    context = {
        'post': post 
    }
    return render(request, 'single.html', context=context)

def contact(request):
    return render(request, 'contact.html')