from django import forms
from django.forms import ModelForm

from .models import Comments, Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [ 'author', 'slug']

class Commentsform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')
