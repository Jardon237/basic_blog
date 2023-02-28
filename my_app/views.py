from django.shortcuts import render
from my_app.models import Post

def home(request,  *args, **kwargs):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)
 
def about(request, *args, **kwargs):
    return render(request, 'about.html', {})