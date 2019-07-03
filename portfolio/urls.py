from django.urls import path
from . import views

urlpatterns = [
    path('software-development/', views.SoftwareProjectsListView.as_view(), name='software_projects_list'),
    path('software-development/<int:pk>/', views.SoftwareProjectDetailView.as_view(), name='software_project_detail'),
    path('civil-engineering/', views.CivilEngineeringProjectsListView.as_view(), name='civil_projects_list'),
    path('civil-engineering/<int:pk>/', views.CivilEngineeringProjectDetailView.as_view(), name='civil_project_detail'),
]
