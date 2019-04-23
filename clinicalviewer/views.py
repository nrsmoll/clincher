from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Main, Visit


class IndexView(ListView):
    template_name = 'clinicalviewer/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Main.objects.all()

class MainView(LoginRequiredMixin, ListView):
    model = Main
    template_name = 'clinicalviewer/home.html'

class DetailView(LoginRequiredMixin, DetailView):
    model = Main
    template_name = 'clinicalviewer/main_detail.html'

class MainCreate(LoginRequiredMixin, CreateView):
    model = Main
    fields = ['firstname', 'lastname', 'date_of_birth']
    template_name = 'clinicalviewer/main_form.html'

class MainUpdate(LoginRequiredMixin, UpdateView):
    model = Main
    fields = ['firstname', 'lastname', 'date_of_birth']

class MainDelete(LoginRequiredMixin, DeleteView):
    model = Main
    success_url = reverse_lazy('clinicalviewer:index')

class VisitCreate(LoginRequiredMixin, CreateView):
    model = Visit
    fields = ['visit_date', 'visit_notes']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.fk_visit_user = self.request.user
        form.fk_visit_main = Main.objects.get(id=self.kwargs['pk'])






















