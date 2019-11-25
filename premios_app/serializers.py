from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = ("id", "author", "title", "description", "publish_date", 
                  "project_pic", "live_site", "reviews") # to add author and reviews


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "projects")