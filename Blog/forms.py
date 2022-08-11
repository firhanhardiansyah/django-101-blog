from django import forms
from django.forms import ModelForm
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_id', 'title', 'author_name']

    blog_id = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Blog Id', 'class': 'form-control mb-3'}
        )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Title', 'class': 'form-control mb-3'}
        )
    )
    author_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Author Name', 'class': 'form-control mb-3'}
        )
    )
