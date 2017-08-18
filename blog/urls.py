# coding:utf-8 _*_

from django.conf.urls import url
from . import views   # 从当前目录导入views模块

app_name = 'blog'

# 将网址和对应的处理函数作为参数传给url()进行绑定，第一个参数使用正则表达式，'^$'表示空字符开始空字符结尾（空串）
urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
               ]