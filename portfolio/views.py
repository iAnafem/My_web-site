from django.views import generic
from .models import Project, ProjectImages, ProjectComment
from django.views.generic.edit import FormView
from .forms import ProjectForm, CommentForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse


class ProjectDetail(FormMixin, generic.DetailView):
    model = Project
    form_class = CommentForm

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = ProjectComment(
                author=request.user,
                body=form.cleaned_data["body"],
                project=self.object
            )
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


class SoftwareProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter(category__name="Software development")
    template_name = 'portfolio/software_projects_index.html'


class SoftwareProjectDetailView(ProjectDetail):
    template_name = 'portfolio/software_project_detail.html'

    def get_success_url(self):
        return reverse('software_project_detail', kwargs={'pk': self.object.pk})


class CivilEngineeringProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter(category__name="Civil engineering")
    template_name = 'portfolio/civil_projects_index.html'


class CivilEngineeringProjectDetailView(ProjectDetail):
    template_name = 'portfolio/civil_project_detail.html'

    def get_success_url(self):
        return reverse('civil_project_detail', kwargs={'pk': self.object.pk})


class ProjectCreateView(PermissionRequiredMixin, FormView):
    model = Project
    form_class = ProjectForm
    permission_required = 'portfolio.project.can_add_project'
    template_name = 'portfolio/project_create.html'

    def get_success_url(self):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        instance = form.save(commit=False)
        if instance.category.name.startswith('Soft'):
            return '../software-development'
        else:
            return '../civil-engineering'

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

