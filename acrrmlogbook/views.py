from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Main, Visit


class IndexView(generic.ListView):
    template_name = 'acrrmlogbook/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Main.objects.all()

class DetailView(generic.DetailView):
    model = Main
    template_name = 'acrrmlogbook/detail.html'

class MainCreate(CreateView):
    model = Main
    fields = ['name', 'date_of_birth']

class MainUpdate(UpdateView):
    model = Main
    fields = ['name', 'date_of_birth']

class MainDelete(DeleteView):
    model = Main
    success_url = reverse_lazy('acrrmlogbook:index')

class VisitCreate(CreateView):
    model = Visit
    fields = ['fk_visit_patient', 'visit_date']





















