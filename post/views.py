
from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DeleteView, UpdateView



class PostList(ListView):
    model = Post


class PostDetail(DeleteView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields =['title','content']
    template_name='post/post_edit.html'
    
