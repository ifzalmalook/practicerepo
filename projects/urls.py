from django.urls import path
from .views import AddProject, Projects, DeleteProject, EditProject
from . import views

urlpatterns = [
    path('', AddProject.as_view(), name='add_project'),
    path('projects/', Projects.as_view(), name='projects'),
    path('<slug:slug>/', views.full_project, name='full_project'),
    path('delete/<slug:slug>/', DeleteProject.as_view(), name='delete_project'),
    path('edit/<slug:slug>/', EditProject.as_view(), name='edit_project'),
    # path('like/<slug:slug>', views.LikeView, name='like_post'),
]