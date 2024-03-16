from django.urls import path
from .views import AddProject, Projects
from . import views

urlpatterns = [
    path('', AddProject.as_view(), name='add_project'),
    path('projects', Projects.as_view(), name='projects'),
    path('<slug:slug>/', views.full_project, name='full_project'),
]