from django.urls import path, re_path
from . import views

urlpatterns = [
    path('software-development/', views.SoftwareProjectsListView.as_view(), name='software_projects_list'),
    path('software-development/<int:pk>/', views.SoftwareProjectDetailView.as_view(), name='software_project_detail'),
    path('civil-engineering/', views.CivilEngineeringProjectsListView.as_view(), name='civil_projects_list'),
    path('civil-engineering/<int:pk>/', views.CivilEngineeringProjectDetailView.as_view(), name='civil_project_detail'),
    path('project-create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('project-comments/<int:pk>/update/', views.UpdateProjectCommentView.as_view(), name='update_project_comment'),
    path('project-comments/<int:pk>/delete/', views.DeleteProjectCommentView.as_view(), name='delete_project_comment'),
    re_path(r'\D+/(?P<pk>\w+)/update/$', views.ProjectUpdateView.as_view(), name='project_update'),
    re_path(r'\D+/(?P<pk>\w+)/delete/$', views.ProjectDeleteView.as_view(), name='project_delete'),
]

