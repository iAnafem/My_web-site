from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogIndex.as_view(), name="blog_index"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    # path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<category>/", views.PostCategory.as_view(), name="post_category"),
]