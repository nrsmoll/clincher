from django import forms
from .models import Main, Visit
from django.forms import ModelForm



class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ('firstname', 'middlename', 'lastname', 'date_of_birth', 'sex', 'address')
        widgets = {
            'date_of_birth': DateInput(),
        }


class VisitForm(forms.Form):
    visit_types_list = (
        (str(1), 'Consultation'),
        (str(2), 'Procedure'),
        (str(3), 'Administrative'),)
    visit_type = forms.ChoiceField(choices=visit_types_list)
    visit_label = forms.CharField(label='Visit Label', max_length=100)
    progress_note = forms.CharField(widget=forms.Textarea)

    def form_valid(self, form):
        form.instance.fk_visit_user = self.request.user
        form.instance.fk_visit_main = Main.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
