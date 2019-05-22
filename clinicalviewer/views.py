from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from .models import Visit
from .forms import VisitForm, PatientForm
from django.contrib.auth import get_user_model

class IndexView(ListView):
    template_name = 'clinicalviewer/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return get_user_model().objects.all()

class PatientView(LoginRequiredMixin, ListView):
    model = get_user_model()
    # context_object_name = 'all_patients' <- object_list is the default name
    template_name = 'clinicalviewer/home.html'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'clinicalviewer/patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['visit_set'] = Visit.objects.all()
        # And so on for more models
        return context

class PatientCreate(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = PatientForm
    template_name = 'clinicalviewer/patient_form.html'

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = PatientForm
    template_name = 'clinicalviewer/patient_form.html'

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('clinicalviewer:index')

class VisitCreate(LoginRequiredMixin, FormMixin, DetailView):
    model = get_user_model()
    form_class = VisitForm
    template_name = 'clinicalviewer/visit_form.html'

    def get_context_data(self, **kwargs):
        context = super(VisitCreate, self).get_context_data(**kwargs)
        context['form'] = VisitForm(initial={'users': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(VisitCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.pk})

class VisitDetail(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = 'clinicalviewer/visit_detail.html'

class VisitDelete(LoginRequiredMixin, DeleteView):
    model = Visit

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.user.pk})




























