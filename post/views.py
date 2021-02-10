
from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DetailView, UpdateView



class PostList(ListView):
    model = Post

    
class PostUpdate(UpdateView):
    model = Post
    fields =['title','content','category']
    template_name='post/post_edit.html'


class PostDetail(DetailView):
    model = Post
    template_name='post/post_details.html'




