from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutIndex.as_view(), name='about-index'),
    path('resume/', views.ResumeIndex.as_view(), name='resume-index'),
    path('contact/', views.ContactIndex.as_view(), name='contact-index'),
]
