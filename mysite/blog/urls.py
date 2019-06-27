from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blog-index'),
]