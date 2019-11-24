from django import forms
from .models import Project, Profile, Review
from tinymce.widgets import TinyMCE

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "project_pic",)
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control mb-4"}),
            "description":TinyMCE(attrs={'cols': 116, 'rows': 15}),
            "project_pic":forms.FileInput(attrs={"class":"custom-file"}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "design_score", "usability_score", "content_score",)
        widgets = {
            "comment":forms.Textarea(attrs={"class":"form-control mb-4"}),
            "design_score":forms.NumberInput(attrs={"class":"form-control mb-4"}),
            "usability_score":forms.NumberInput(attrs={"class":"form-control mb-4"}),
            "content_score":forms.NumberInput(attrs={"class":"form-control mb-4"}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")
        widgets = {
            "bio":forms.Textarea(attrs={"class":""}),
            "profile_pic":forms.FileInput(attrs={"class":""}),
        }
