from django import forms
from django.forms import ModelForm
from .models import Post



class AddBlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','category','post_image')