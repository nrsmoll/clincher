from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        (str(1), 'Male'),
        (str(2), 'Female'))
    sex = models.CharField(choices=GENDER_CHOICES, max_length=30, blank=True, null=True)
    has_appointment = models.BooleanField(default=False)
    is_waiting = models.BooleanField(default=False)

    app_label='auth'

    # Redirects after form is submitted using primary key
    def get_absolute_url(self):
        return reverse('clinicalviewer:profile-detail', kwargs={'pk': self.pk})

    #def __str__(self):
        #return self.firstname + ' ' + self.lastname + ' - ' + str(self.date_of_birth)
