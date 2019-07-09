from django import forms
from .models import Project


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter project title"
        })
    )
    content_images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter a short description"
        })
    )

    technologies = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the names of the technologies used"
        })
    )

    full_description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter a full description"
        })
    )

    class Meta:
        model = Project
        fields = '__all__'

