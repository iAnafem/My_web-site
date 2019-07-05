from django.urls import reverse_lazy, reverse
# from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(generic.FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home_page_index')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('home_page_index'))


class UserDetailView(generic.DetailView):
    model = CustomUser
    template_name = 'accounts/profile_detail.html'
