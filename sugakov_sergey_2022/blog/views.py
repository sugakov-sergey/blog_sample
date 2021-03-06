from django.shortcuts import render
from .models import Post, Comment


# Create your views here.

# def project(request):
#     return render(request, 'project.html')

def blog_index(request):
    posts = Post.objects.all()
    context = {'posts': posts.order_by('-created_on')}  # сортировка "-" в обратном направлении
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'blog_detail.html', context)