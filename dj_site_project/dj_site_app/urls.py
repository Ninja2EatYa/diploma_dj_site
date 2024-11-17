from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('projects_list/', projects_list, name='projects_list'),
    # path('projects_list/projects/', projects, name='projects'),
    path('contacts/', contacts, name='contacts'),
]