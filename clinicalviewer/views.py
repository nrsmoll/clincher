from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from .models import Encounter, Pasthx, EncounterReason
from .forms import EncounterForm, PatientForm, PasthxForm
from django.contrib.auth import get_user_model

from dal import autocomplete



class IndexView(ListView):
    template_name = 'clinicalviewer/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return get_user_model().objects.all()

class PatientView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'clinicalviewer/home.html'
    queryset=get_user_model().objects.filter(is_staff=False)
    # context_object_name = 'all_patients' <- because object_list is the default name



class PatientDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'clinicalviewer/patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['encounter_set'] = Encounter.objects.filter(patid=self.object)
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

class EncounterCreate(LoginRequiredMixin, FormMixin, DetailView):
    model = get_user_model()
    form_class = EncounterForm
    template_name = 'clinicalviewer/encounter_form.html'


    def get_context_data(self, **kwargs):
        context = super(EncounterCreate, self).get_context_data(**kwargs)
        context['form'] = EncounterForm(initial={'patid': self.object})
        context['encounter_set'] = Encounter.objects.filter(patid=self.object)
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
        return super(EncounterCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.pk})


class EncounterDetail(LoginRequiredMixin, DetailView):
    model = Encounter
    template_name = 'clinicalviewer/encounter_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EncounterDetail, self).get_context_data(**kwargs)
        #reverse lookup
        encounter_set = Encounter.objects.filter(patid=self.patid)
        context.update({'encounter_set': encounter_set})
        #context['visit_set'] = Encounter.objects.filter(patid=self.patid)
        # And so on for more models
        return context

class EncounterDelete(LoginRequiredMixin, DeleteView):
    model = Encounter

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.patid.pk})




class PasthxCreate(LoginRequiredMixin, FormMixin, DetailView):
    model = get_user_model()
    form_class = PasthxForm
    template_name = 'clinicalviewer/pasthx_form.html'

    def get_context_data(self, **kwargs):
        context = super(PasthxCreate, self).get_context_data(**kwargs)
        context['form'] = PasthxForm(initial={'patid': self.object})
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
        return super(PasthxCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.pk})


class PasthxDetail(LoginRequiredMixin, DetailView):
    model = Encounter
    template_name = 'clinicalviewer/pasthx_detail.html'

class PasthxDelete(LoginRequiredMixin, DeleteView):
    model = Pasthx

    def get_success_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.object.patid.pk})








class EncounterReasonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return EncounterReason.objects.none()
        qs = EncounterReason.objects.all()
        if self.q:
            qs = qs.filter(reason__istartswith=self.q)
        return qs






