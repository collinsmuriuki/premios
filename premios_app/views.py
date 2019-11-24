from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project, Review, User
from .forms import ProjectForm, ReviewForm, UpdateProfileForm
from django.utils import timezone
from django.urls import reverse_lazy

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


class ProjectCreate(CreateView): # add loginrequiredmixin
    model = Project
    form_class = ProjectForm


class ProjectUpdate(UpdateView):  # add loginrequiredmixin
    model = Project
    form_class = ProjectForm


class ProjectDelete(DeleteView):   # add loginrequiredmixin
    model = Project
    success_url = reverse_lazy("post_list")


class UserDetail(DetailView): 
    model = User
    context_object_name = "user"


class UserProfileUpdate(UpdateView):   # add loginrequiredmixin
    model = User
    form_class = UpdateProfileForm


# @login_required
def review_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    current_user = request.user

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.author = current_user
            review.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ReviewForm()
    return render(request, "premios_app/review_form.html", context={"form":form,
                                                                    "project":project})

# @login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    project_pk = review.project.pk
    review.delete()
    return redirect("project_detail", pk=project_pk)         