# _*_ coding:utf-8 _*_

from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# 分类表
class Category(models.Model):
    #   id属性Django会自动创建
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 文章表
class Post(models.Model):
    #   文章属性定义
    title = models.CharField(max_length=50)
    body = models.TextField()   # 存储博客正文，是一段大文本
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField(blank=True)
    excerpt = models.CharField(max_length=200, blank=True)   # 文章摘要，blank=True表示可以为空

    # 关联关系说明
    category = models.ForeignKey(Category)  # 一篇文章只属于一个类，一个类可以有多篇文章
    tags = models.ManyToManyField(Tag, blank=True)   # 一篇文章有多个标签，一个标签属于多个文章

    # 作者,同时也是用户，使用Django内置对象
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title + '(作者:' + self.author.username + ')'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})