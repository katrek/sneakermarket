from django.views.generic import TemplateView, ListView


from sneakers.models import Sneakers

class AboutPage(TemplateView):
    template_name = 'about.html'


class HomepageView(ListView):
    model = Sneakers
    template_name = 'index.html'
    context_object_name = 'sneakers'
    paginate_by = 3
    ordering = ['-pk']
    #
    #
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomepageView, self).get_context_data(*args, **kwargs)
    #     context['sneakers'] = Sneakers.objects.all()
    #
    #     return context




