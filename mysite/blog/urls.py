from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogIndex.as_view(), name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]