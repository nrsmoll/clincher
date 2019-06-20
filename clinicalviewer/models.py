from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import Users

# Create your models here.
class Visit(models.Model):
    patid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=('Patient Name'), related_name='visit_patid')
    created_by = models.ForeignKey(Users, editable=False, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='visit_created_by')
    visit_date = models.DateField()
    visit_label = models.CharField(max_length=256, blank=True, null=True)
    visit_types_list = (
        (str(1), 'Progress'),
        (str(2), 'Procedure'),
        (str(3), 'Admin'),)
    visit_type = models.CharField(
        max_length=256,
        choices=visit_types_list,
        default=1,)
    visit_notes = models.TextField(max_length=50000,
                                   blank=True)
    date_of_entry = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return str(self.visit_label)

    def get_absolute_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.pk})


class Pasthx(models.Model):
    patid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=('Patient Name'), related_name='pasthx_patid')
    created_by = models.ForeignKey(Users, editable=False, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='pasthx_created_by')
    pasthx_date_diagnosis = models.DateField()
    diagnosis = models.CharField(max_length=256, blank=True, null=True)
    is_active = models.BooleanField()
    pasthx_notes = models.TextField(max_length=50000,
                                   blank=True)
    date_of_entry = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return str(self.diagnosis)

    def get_absolute_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.pk})