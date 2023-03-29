from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from.forms import Commentsform, Postform

form = Commentsform

def home(request,  *args, **kwargs):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)
 
def about(request, *args, **kwargs):
    return render(request, 'about.html', {})

def detail(requst, slug):
    post = get_object_or_404(Post, slug=slug)
    context={
        'post': post
    }
    return(render, 'detail.html', context)

def new_post(request):
    if request.method == "POST":
        form = Postform(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            form = Postform()
    context={
        'form': form
    }

    return render(request, 'new_post.html',context)
        

