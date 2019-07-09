from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name="blog_index"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('create/', views.CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/update/', views.UpdatePostView.as_view(), name='update_post'),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('<category>/', views.PostCategory.as_view(), name="post_category"),
    path('authors/<author>/', views.PostAuthor.as_view(), name="post_author"),
    path('comments/<int:pk>/update/', views.UpdateCommentView.as_view(), name='update_comment'),
    path('comments/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete_comment'),
]
