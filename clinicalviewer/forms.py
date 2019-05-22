from django import forms
from .models import Visit
from django.forms import ModelForm, Form
import datetime
from django.contrib.auth import get_user_model

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex', 'address', 'medicare1', 'medicare2')
        widgets = {
            'date_of_birth': DateInput(),
        }



class VisitForm(forms.ModelForm):
    visit_date = forms.DateField(initial=datetime.date.today, widget = DateInput())
    class Meta:
        model = Visit
        fields = ('__all__')
