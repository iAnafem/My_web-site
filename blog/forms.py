from django import forms
from .models import Comment, Post, Category


class CommentForm(forms.Form):

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Type a title"
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Type a text"
        })
    )

    class Meta:
        model = Post
        exclude = ('author',)


