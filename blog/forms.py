from django import forms
from .models import Comment, Post


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

    class Meta:
        model = Post
        fields = '__all__'


