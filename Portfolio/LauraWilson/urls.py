from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('resume', views.resume, name='resume'),
    path('projects', views.projects, name='projects'),
    path('corpus', views.corpus, name='corpus'),

]