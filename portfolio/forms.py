from django import forms
from .models import Project, ProjectComment


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

    class Meta:
        model = ProjectComment
        fields = ('body',)


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
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the names of the technologies used"
        }),
    )

    full_description = forms.CharField(
        max_length=2500,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter a full description"
        }),
        required=False,
    )

    full_description_2 = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter a full description"
        }),
        required=False,
    )

    class Meta:
        model = Project
        exclude = ('content_images',)


class UpdateProjectForm(ProjectForm):
    model = Project
    exclude = ('content_images',)


class UpdateCommentForm(CommentForm, forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
