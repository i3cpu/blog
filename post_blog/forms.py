from django import forms
from post_blog.models import Post
from post_blog.models import Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']