from .forms import CommentForm, PostForm
from django.views import generic
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


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
        # Add in the publisher
        context['category'] = self.categories
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
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
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


class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/users/login/'
    model = Post
    # permission_required = 'catalog.can_create_posts'
    fields = '__all__'


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    login_url = '/users/login/'
    model = Post
    # permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('blog_index')


"""
class PostDisplay(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj


class CommentPost(generic.detail.SingleObjectMixin, generic.FormView):
    template_name = 'blog/post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetail(View):
    model = Post

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
"""