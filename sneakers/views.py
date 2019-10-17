from django.views.generic import ListView, DetailView, CreateView
from .models import Sneakers
from .forms import SneakersForm


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



