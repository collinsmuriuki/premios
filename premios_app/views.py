from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project, Review, User
from django.utils import timezone

# Create your views here.

class AboutView(TemplateView):
    template_name = "premios_app/about.html"


class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(publish_date__lte=timezone.now()).order_by("-publish_date")


class ProjectDetail(DetailView):
    model = Project
    context_object_name = "project"


class UserDetail(DetailView):
    model = User
    context_object_name = "user"
    