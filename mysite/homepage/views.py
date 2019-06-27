from django.views import generic
from .models import Home


class HomeIndex(generic.ListView):
    model = Home
    queryset = Home.objects.all()
    template_name = 'homepage/home_index.html'




