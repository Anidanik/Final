from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class RegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


class Logout(LogoutView):
    next_page = 'login'


