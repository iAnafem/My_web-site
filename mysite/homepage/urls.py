from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home_index"),
]
