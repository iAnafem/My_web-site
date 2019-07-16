from django.views import generic
from .models import Project, ProjectImages, ProjectComment
from django.views.generic.edit import FormView
from .forms import ProjectForm, CommentForm, UpdateProjectForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse
from blog.views import CheckDeletePermissions, CheckUpdatePermissions


class ProjectDetail(FormMixin, generic.DetailView):
    model = Project
    form_class = CommentForm

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['count'] = ""
        for i in range(1, len(self.get_object().content_images.all())):
            context['count'] += str(i)
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
    template_name = 'portfolio/software_projects_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Project.objects.filter(category__name="Software development")
        count = len(queryset)
        context['cards'] = list()
        for i in range(0, count - count % 3, 3):
            context['cards'].append(queryset[i:i + 3])
        context['last_card'] = queryset[(count - count % 3):count]
        return context


class SoftwareProjectDetailView(ProjectDetail):
    template_name = 'portfolio/software_project_detail.html'

    def get_success_url(self):
        return reverse('software_project_detail', kwargs={'pk': self.object.pk})


class CivilEngineeringProjectsListView(generic.ListView):
    model = Project
    template_name = 'portfolio/civil_projects_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Project.objects.filter(category__name="Civil engineering")
        count = len(queryset)
        context['cards'] = list()
        for i in range(0, count - count % 3, 3):
            context['cards'].append(queryset[i:i + 3])
        context['last_card'] = queryset[(count - count % 3):count]
        return context


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


class ProjectUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Project
    permission_required = 'portfolio.project.can_change_project'
    form_class = UpdateProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['content_images'] = ProjectImages.objects.filter(project=self.object.pk)
        return context

    def get_success_url(self):
        """Returns the url to access a particular post instance."""
        if self.get_object().category.name.startswith('Soft'):
            return reverse('software_project_detail', kwargs={'pk': self.object.pk})
        else:
            return reverse('civil_project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Project
    permission_required = 'portfolio.project.can_delete_project'

    def get_success_url(self):
        """Returns the url to access a particular post instance."""
        if self.get_object().category.name.startswith('Soft'):
            return reverse('software_projects_list')
        else:
            return reverse('civil_projects_list')


class UpdateProjectCommentView(CheckUpdatePermissions):
    model = ProjectComment
    fields = ('body', )


class DeleteProjectCommentView(CheckDeletePermissions):
    model = ProjectComment

    def get_success_url(self):
        """Returns the url to access a particular project instance."""
        if self.get_object().project.category.name.startswith('Soft'):
            return reverse('software_project_detail', kwargs={'pk': self.object.project.pk})
        else:
            return reverse('civil_project_detail', kwargs={'pk': self.object.project.pk})
