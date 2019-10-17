from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, TemplateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from sneakers.models import Sneakers
from .forms import CustomUserCreationForm, CustomUserChangeForm




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class UserProfileView(LoginRequiredMixin, DetailView):
#     template_name = 'user_profile.html'
#     model = CustomUser
#     login_url = 'login'
#     context_object_name = 'user'


class SingleUserView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'single_user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SingleUserView, self).get_context_data(
            *args, **kwargs)
        context['sneakers'] = Sneakers.objects.filter(author=self.request.user)

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('single-user-profile')
    login_url = 'login'

    def get_object(self):
        return self.request.user


class UserListView(ListView):
    model = CustomUser
    template_name = 'users_list.html'
    context_object_name = 'users'
    paginate_by = 10