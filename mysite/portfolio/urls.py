from django.urls import path
from . import views

urlpatterns = [
    path('', views.SoftwareProjectsListView.as_view(), name='software_projects_list'),
    path('project/<int:pk>/', views.SoftwareProjectDetailView.as_view(), name='software_project_detail'),
]
