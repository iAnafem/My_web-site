from django.views import generic
from .models import Project, ProjectImages
from django.views.generic.edit import FormView
from .forms import ProjectForm
from django import forms

class SoftwareProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter(category__name="Software development")
    template_name = 'portfolio/software_projects_index.html'


class SoftwareProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/software_project_detail.html'


class CivilEngineeringProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter(category__name="Civil engineering")
    template_name = 'portfolio/civil_projects_index.html'


class CivilEngineeringProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/civil_project_detail.html'


class ProjectCreateView(FormView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_create.html'
    success_url = '/'

    """
    from portfolio.models import ProjectImages
    ProjectImages.objects.all().delete()
    
    """

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('content_images')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            for file in files:
                ProjectImages.objects.create(
                    image=file,
                    project=instance,
                )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
