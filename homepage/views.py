from django.views import generic
from .models import HomePage


class HomePageContent(generic.ListView):
    model = HomePage
    queryset = HomePage.objects.all()
    template_name = 'homepage/home_page_index.html'

