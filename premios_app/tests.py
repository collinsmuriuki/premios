from django.test import TestCase
from .models import Profile, Project, Review
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

class ProfileTest(TestCase):
    
    def setUp(self):
        self.new_user = User(username="collins", email="collins@gmail.com",
                             password="saf3ty")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, bio="Hello World",
                                   profile_pic="profile_pics/default.png")
        self.new_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        self.new_profile.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)


class ProjectTest(TestCase):

    def setUp(self):
        self.new_user = User(username="collins", email="collins@gmail.com",
                             password="saf3ty")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, bio="Hello World",
                                   profile_pic="profile_pics/default.png")
        self.new_profile.save()
        self.new_project = Project(author=self.new_user, title="Random Title",
                                   description="Random description", live_site="google.com")
        self.new_project.save()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save_project(self):
        self.new_project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_search_project(self):
        self.new_project.save()
        searched_project = Project.search_projects("Random Title")
        self.assertTrue(len(searched_project)==1)

    
class ReviewTest(TestCase):

    def setUp(self):
        self.new_user = User(username="collins", email="collins@gmail.com",
                             password="saf3ty")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, bio="Hello World",
                                   profile_pic="profile_pics/default.png")
        self.new_profile.save()
        self.new_project = Project(author=self.new_user, title="Random Title",
                                   description="Random description", live_site="google.com")
        self.new_project.save()
        self.new_review = Review(project=self.new_project, author=self.new_user,
                                 comment="Nice", design_score=9, usability_score=9,
                                 content_score=9)
        self.new_review.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))

    def test_save_review(self):
        self.new_review.save()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_get_average_score(self):
        average_score = self.new_review.get_average_score()
        self.assertEqual(average_score, 9)