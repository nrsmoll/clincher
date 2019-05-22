from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Visit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=('Patient Name'))
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