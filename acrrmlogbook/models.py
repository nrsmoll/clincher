from django.db import models
from django.urls import reverse

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length = 256)
    date_of_birth = models.CharField(max_length = 256)

    #Redirects after form is submitted using primary key
    def get_absolute_url(self):
        return reverse('acrrmlogbook:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' - ' + self.date_of_birth


class Visit(models.Model):
    fk_visit_patient = models.ForeignKey(Main, on_delete=models.CASCADE, verbose_name=('Patient Name'))
    visit_date = models.DateField()
    visit_label = models.CharField(max_length=256, blank=True, null=True)
    visit_types_list = (
        (str(1), 'Consultation'),
        (str(2), 'Procedure'),)
    visit_type = models.CharField(
        max_length=256,
        choices=visit_types_list,
        default=1,)
    visit_specialty_list = (
        (str(1), 'General Practice'),
        (str(2), 'Internal Medicine'),
        (str(3), 'Surgery'),
        (str(4), 'Obstetrics & Gynaecology'),
        (str(5), 'Anesthetics'),
        (str(6), 'Paediatrics'),
        (str(7), 'Mental Health'),
        (str(8), 'Opthalmology'),
        (str(9), 'Orthopedics'),
        (str(10), 'Trauma'),)
    visit_specialty = models.CharField(
        max_length=256,
        choices=visit_specialty_list,
        default=1, )
    visit_notes = models.TextField(max_length=10000,
                                   blank=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.visit_label)

    def get_absolute_url(self):
        return reverse('acrrmlogbook:detail', kwargs={'pk': self.pk})