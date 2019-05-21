from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.urls import reverse_lazy, reverse
from .models import Profile, Visit
from .forms import VisitForm, ProfileForm


class IndexView(ListView):
    template_name = 'clinicalviewer/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Profile.objects.all()

class ProfileView(LoginRequiredMixin, ListView):
    model = Profile
    # context_object_name = 'all_patients' <- object_list is the default name
    template_name = 'clinicalviewer/home.html'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'clinicalviewer/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['visit_set'] = Visit.objects.all()
        # And so on for more models
        return context

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'clinicalviewer/profile_form.html'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['firstname', 'lastname', 'date_of_birth']

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('clinicalviewer:index')

class VisitCreate(LoginRequiredMixin, FormMixin, DetailView):
    model = Profile
    form_class = VisitForm
    template_name = 'clinicalviewer/visit_form.html'

    def get_context_data(self, **kwargs):
        context = super(VisitCreate, self).get_context_data(**kwargs)
        context['form'] = VisitForm(initial={'fk_visit_profile': self.object})
        #context['visit_set'] = Visit.objects.select_related('fk_visit_profile').all()
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
        return reverse('clinicalviewer:profile-detail', kwargs={'pk': self.object.pk})

class VisitDetail(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = 'clinicalviewer/visit_detail.html'

class VisitDelete(LoginRequiredMixin, DeleteView):
    model = Visit

    def get_success_url(self):
        return reverse('clinicalviewer:profile-detail', kwargs={'pk': self.object.fk_visit_profile.pk})




























