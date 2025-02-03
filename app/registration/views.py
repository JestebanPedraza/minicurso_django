from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = './signup.html'
    success_url = reverse_lazy('registration:signup')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class SignInView(LoginView):
    template_name = './signin.html'
    authentication_form = UserAuthenticationForm
    success_url = reverse_lazy('registration:signup')

    def get_success_url(self):
        return self.success_url
