from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.forms import ModelChoiceField


class PostForm(forms.ModelForm):
    
    author = ModelChoiceField(queryset=User.objects.all())
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')


        widgets={
            'title':forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable meduim-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets= {
            'author':forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text':forms.Textarea(attrs = {'class': 'editable medium-textarea'}),
        }