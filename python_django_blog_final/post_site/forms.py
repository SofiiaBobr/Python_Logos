from django import forms
from django.forms import ModelForm
from .models import Post, Category, Comment


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        labels = {
            'title': '',
            'title_tag': '',
            'author': '',
            'category': '',
            'body': '',
            'snippet': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Author', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),

        }


class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        labels = {
            'title': '',
            'title_tag': '',
            'author': '',
            'body': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        labels = {
            'name': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        labels = {
            'name': '',
            'body': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        }
