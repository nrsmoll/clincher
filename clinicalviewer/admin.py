from django.contrib import admin
from .models import Profile, Visit
# Register your models here.



class VisitAdmin(admin.ModelAdmin):
    list_display = ['fk_visit_profile', 'visit_label', 'visit_date', 'visit_type',]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'date_of_birth', 'is_waiting',]
    list_filter = ['firstname', 'lastname', 'date_of_birth', 'is_waiting',]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Visit, VisitAdmin)