from django import forms
from .models import Profile, Visit
from django.forms import ModelForm, Form
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('firstname', 'middlename', 'lastname', 'date_of_birth', 'sex',)
        widgets = {
            'date_of_birth': DateInput(),
        }



class VisitForm2(Form):
    visit_types_list = (
        (str(1), 'Consultation'),
        (str(2), 'Procedure'),
        (str(3), 'Administrative'),)
    visit_type = forms.ChoiceField(choices=visit_types_list)
    visit_label = forms.CharField(label='Visit Label', max_length=100)
    progress_note = forms.CharField(widget=forms.Textarea)

    def form_valid(self, form):
        form.instance.fk_visit_profile = Profile.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)



class VisitForm(forms.ModelForm):
    visit_date = forms.DateField(initial=datetime.date.today, widget = DateInput())
    class Meta:
        model = Visit
        fields = ('__all__')
