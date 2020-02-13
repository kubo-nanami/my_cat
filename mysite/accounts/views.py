from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.views import generic

from .form import LoginForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class LoginView(generic.CreateView):
    form_class = LoginForm
    success_url = reverse_lazy
    template_name = 'account/login.html'

    def users_detail(self, request):
        user = request.user
        return render(request, 'polls/management_list.html', {'user':user})

class LogoutView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('logout')