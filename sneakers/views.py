from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Sneakers
from .forms import SneakersForm
from django.urls import reverse_lazy



class SneakersView(ListView):
    model = Sneakers
    template_name = 'sneakers.html'
    context_object_name = 'sneakers'
    paginate_by = 6
    ordering = ['-pk']


class SneakerDetailView(DetailView):
    model = Sneakers
    template_name = 'sneakers_details.html'
    context_object_name = 'sneakers'


class SneakerCreateView(CreateView):
    model = Sneakers
    template_name = 'add_sneakers.html'
    context_object_name = 'sneakers'
    form_class = SneakersForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SneakerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sneakers
    template_name = 'sneakers_delete.html'
    success_url = reverse_lazy('sneakers')
    login_url = 'login'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class SneakerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'sneakers_edit.html'
    model = Sneakers
    fields = ['model_name', 'model_price', 'model_photo']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


