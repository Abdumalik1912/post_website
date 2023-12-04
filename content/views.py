from django.shortcuts import render
from .models import Post, Images


def homepage(request):
    posts = Post.objects.all()
    images = Images.objects.all()
    return render(request, "index.html", context={"posts": posts, "images": images})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    images = Images.objects.all()
    return render(request, "post_page.html", context={"posts": posts, "images": images})
