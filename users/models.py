from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

class Users(AbstractUser):
    date_of_birth = models.DateField(blank=True,
                                     null=True,
                                     help_text="Please use the following format: <em>DD-MM-YYYY</em>.")
    middle_name = models.CharField(max_length=30, blank=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=20, blank=True, null=True)
    has_appointment = models.BooleanField(default=False, blank=True)
    is_waiting = models.BooleanField(default=False)
    address = models.TextField(blank=True)
    medicare1 = models.IntegerField(null=True, blank=True)
    medicare2 = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    app_label='auth'

    def get_absolute_url(self):
        return reverse('clinicalviewer:patient-detail', kwargs={'pk': self.pk})
