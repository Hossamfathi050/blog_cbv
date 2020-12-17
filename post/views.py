from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request):
    all_posts= Post.objects.all()
    print("Hossam Fathi")
    return render(request,'post/post_list.html',{'all_posts': all_posts})


def post_details(request,id):
    post= Post.objects.get(id=id)
    return render(request,'post/post_details.html',{'post':post})


def post_create(requestd):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PostForm()    
    return render(request,'post/Post_create.html' , {'form':form})


def post_edit(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form= PostForm(request.POST ,instance=post)
        if form.is_valid():
            form.save()
    else:
        form=PostForm(instance=post)    
    return render(request,'post/post_edit.html' , {'form':form})
    