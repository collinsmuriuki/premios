from django import forms
from .models import Project, Profile, Review

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "project_pic",)
        widgets = {
            "title":forms.TextInput(attrs={"class":""}),
            "description":forms.Textarea(attrs={"class":""}),
            "project_pic":forms.FileInput(attrs={"class":""}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "design_score", "usability_score", "content_score",)
        widgets = {
            "comment":forms.Textarea(attrs={"class":""}),
            "design_score":forms.NumberInput(attrs={"class":""}),
            "usability_score":forms.NumberInput(attrs={"class":""}),
            "content_score":forms.NumberInput(attrs={"class":""}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")
        widgets = {
            "bio":forms.Textarea(attrs={"class":""}),
            "profile_pic":forms.FileInput(attrs={"class":""}),
        }
