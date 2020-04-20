from django.views.generic import ListView, DetailView
from cooperatives.models import Cooperative


class CooperativeListView(ListView):
    model = Cooperative
    template_name = 'cooperatives/list.html'


class CooperativeDetailView(DetailView):
    model = Cooperative
    template_name = 'cooperatives/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
