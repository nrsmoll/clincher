from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length = 256)
    middlename = models.CharField(max_length = 256)
    lastname = models.CharField(max_length=256)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30, blank=True, null=True)
    has_appointment = models.BooleanField(default=False)
    is_waiting = models.BooleanField(default=False)

    #Redirects after form is submitted using primary key
    def get_absolute_url(self):
        return reverse('clinicalviewer:profile-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' - ' + str(self.date_of_birth)


class Visit(models.Model):
    fk_visit_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=('Patient Name'))
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
        return reverse('clinicalviewer:profile-detail', kwargs={'pk': self.pk})