from django.views import generic
from .models import Blog


class BlogIndex(generic.ListView):
    model = Blog
    template_name = 'blog/blog_index.html'
