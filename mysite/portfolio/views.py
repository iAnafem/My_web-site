from django.views import generic
from .models import Project


class SoftwareProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter(category__name="Software development")
    template_name = 'portfolio/software_projects_index.html'


class SoftwareProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/software_project_detail.html'
