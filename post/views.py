from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView

# Create your views here.
from .models import Post


class PostList(ListView):
    model = Post


class PostDetail(DeleteView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields =['title','content']
    template_name='post/post_edit.html'
    

