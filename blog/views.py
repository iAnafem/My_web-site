from .forms import CommentForm, PostForm
from django.views import generic
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from accounts.models import CustomUser


class BlogIndex(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = "blog/blog_index.html"


class PostCategory(generic.ListView):

    template_name = "blog/post_category.html"

    def get_queryset(self):
        self.categories = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(categories=self.categories).order_by(
            '-created_on'
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the category
        context['category'] = self.categories
        return context


class PostAuthor(generic.ListView):
    template_name = "blog/post_author.html"

    def get_queryset(self):
        author_id = CustomUser.objects.filter(username=self.kwargs['author']).values('id')[0]['id']
        return Post.objects.filter(author=author_id).order_by(
            '-created_on'
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the author
        context['author'] = self.kwargs['author']
        return context


class PostDetail(FormMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

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
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=self.object
            )
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/login/'
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog_index')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CheckUpdatePermissions(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = '/users/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CheckDeletePermissions(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    login_url = '/users/login/'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class UpdatePostView(CheckUpdatePermissions):
    model = Post
    fields = '__all__'


class DeletePostView(CheckDeletePermissions):
    model = Post
    success_url = reverse_lazy('blog_index')


class UpdateCommentView(UpdatePostView):
    model = Comment
    fields = ('body', )


class DeleteCommentView(CheckDeletePermissions):
    model = Comment

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
