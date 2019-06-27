from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageContent.as_view(), name="home_page_index"),
]
