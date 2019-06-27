from django.views import generic
from .models import About, Resume, Contact


class AboutIndex(generic.ListView):
    model = About
    template_name = 'infopages/about_index.html'


class ResumeIndex(generic.ListView):
    model = Resume
    template_name = 'infopages/resume_index.html'


class ContactIndex(generic.ListView):
    model = Contact
    template_name = 'infopages/contact_index.html'

