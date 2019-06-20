from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from .models import Visit
from .forms import VisitForm, PatientForm, PasthxForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

