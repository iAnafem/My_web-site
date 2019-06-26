from . import views
from django.urls import path

urlpatterns = [
    path('', views.SoftwareProjectsListView.as_view(), name='software_projects_list'),
]
