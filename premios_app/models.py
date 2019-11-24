from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from star_ratings.models import Rating
import statistics

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/")

    def save_profile(self):
        self.save()

    def get_user_projects(self):
        return self.projects.all

    def __str__(self):
        return self.username


class Project(models.Model):
    author = models.ForeignKey(User, related_name="projects")
    title = models.CharField(max_length=144)
    description = models.TextField()
    project_pic = models.ImageField(upload_to="project_pics")
    publish_date = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.title


class Review(models.Model):
    project = models.ForeignKey(Project, related_name="reviews")
    author = models.ForeignKey(User, related_name="reviews")
    comment = models.TextField()
    design_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    star_rating = GenericRelation(Rating, related_query_name='ratings')

    def save_review(self):
        self.save()

    def get_average_score(self):
        return round(statistics.mean([self.design_score, self.usability_score, self.content_score]),1)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.comment