from django.conf.urls import url
from premios_app import views

urlpatterns =[
    url(r"^$", views.ProjectList.as_view(), name="project_list"),
    url(r"^project/(?P<pk>\d+)$", views.ProjectDetail.as_view(), name="project_detail"),
    url(r"^profile/(?P<pk>\d+)$", views.UserDetail.as_view(), name="user_detail"),
    url(r"^about/$", views.AboutView.as_view(), name="about"),
]