from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, Det

# Create your views here.
from .models import Post





class PostList(ListView):
    model = Post


class PostDetail(ListView):
    model = Post


