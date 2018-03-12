from django.contrib import admin
from .models import Main, Visit
# Register your models here.



class VisitAdmin(admin.ModelAdmin):
    list_display = ['fk_visit_patient', 'visit_label', 'visit_date', 'visit_type', 'visit_specialty', 'is_favorite']

admin.site.register(Main)
admin.site.register(Visit, VisitAdmin)