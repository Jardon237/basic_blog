from django.db import models
from django.contrib.auth.models import User
from django .urls import reverse
from django.utils import timezone

class Post(models.Model):

     
                                               
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='draft')
    
    def get_absolute_url(self):
        return reverse('')
    class Meta: 
        ordering = ('-created_at'), 

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
