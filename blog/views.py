# _*_ coding:utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post, Tag, Category

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # render函数根据传入的参数构造HttpResponse对象
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})