from django.shortcuts import get_object_or_404, render
from .models import Post




def home(request):


    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

'''def detail(request, post):
    post = get_object_or_404(Post, slug=post)
    context={
        'post': post
    }
    return(request, 'detail.html', context)'''

def about(request):
    return render(request,'about.html')