from django.urls import path
from .views import AddProject, Projects

urlpatterns = [
    path('', AddProject.as_view(), name='add_project'),
    path('projects', Projects.as_view(), name='projects')
]