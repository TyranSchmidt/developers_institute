from django.forms import ModelForm
from .models import Forum, Comment
from django import forms

class ForumForm(ModelForm):
    class Meta():
        model = Forum
        fields = ['title', 'desc']

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ['desc']
        widgets = {'desc':forms.Textarea(
            attrs={'class': 'form-control', 'name': 'desc', 'rows': 3})}
        labels = {'desc': 'Post a comment'}