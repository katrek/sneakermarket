from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from sneakers.models import Sneakers
from .forms import CustomUserCreationForm, CustomUserChangeForm




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    model = CustomUser
    login_url = 'login'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(
            *args, **kwargs)
        context['sneakers'] = Sneakers.objects.filter(author=self.request.user)

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def get_object(self):
        return self.request.user
