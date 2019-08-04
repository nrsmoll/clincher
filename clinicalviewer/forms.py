from django import forms
from .models import Encounter, Pasthx, EncounterReason
from django.forms import ModelForm, Form
import datetime
from django.contrib.auth import get_user_model
from dal import autocomplete

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex', 'email', 'address', 'medicare1', 'medicare2')
        widgets = {
            'date_of_birth': DateInput(),
        }


class EncounterForm(forms.ModelForm):
    encounter_date = forms.DateField(initial=datetime.date.today, widget = DateInput())
    encounter_notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Encounter Notes', 'id': 'editor', 'rows':50, 'cols':25}))
    encounter_label = forms.ModelChoiceField(queryset=EncounterReason.objects.all(),
        widget=autocomplete.ModelSelect2(url='encounterreason-autocomplete')
    )

    class Meta:
        model = Encounter
        fields = ('__all__')



class PasthxForm(forms.ModelForm):
    class Meta:
        model = Pasthx
        fields = ('__all__')
        widgets = {
            'pasthx_date_diagnosis': DateInput(),
        }