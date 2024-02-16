from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry, Comment

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    
    
class EntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['title', 'content', 'image_url']
    widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
    

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['body']
    widgets = {
          'body': forms.Textarea(attrs={'class': 'form-control'}),
        }