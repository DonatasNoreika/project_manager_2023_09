from django.urls import path
from .views import (ProjectListView,
                    ProjectDetailView,
                    UserProjectListView,
                    ProjectCreateView,
                    ProjectDeleteView,
                    ProjectUpdateView,
                    JobCreateView)

urlpatterns = [
    path('', ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="project"),
    path('userprojects/', UserProjectListView.as_view(), name="userprojects"),
    path('projects/create/', ProjectCreateView.as_view(), name="project_create"),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name="project_delete"),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name="project_update"),
    path('projects/<int:order_id>/createjob/', JobCreateView.as_view(), name="job_create"),
]