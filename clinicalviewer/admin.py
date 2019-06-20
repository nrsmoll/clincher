from django.contrib import admin
from .models import Visit
# Register your models here.



class VisitAdmin(admin.ModelAdmin):
    list_display = ['patid', 'visit_label', 'visit_date', 'visit_type',]


admin.site.register(Visit, VisitAdmin)