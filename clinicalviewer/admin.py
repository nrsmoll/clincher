from django.contrib import admin
from .models import Encounter, EncounterReason
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.



class EncounterAdmin(admin.ModelAdmin):
    list_display = ['patid', 'encounter_label', 'encounter_date', 'encounter_type',]



class EncounterReasonResource(resources.ModelResource):
    class Meta:
        model = EncounterReason


class EncounterReasonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EncounterReasonResource
    fields = [('uid', 'reason', 'valueset_id')]
    list_display = ('reason', 'valueset_id')


admin.site.register(Encounter, EncounterAdmin)
admin.site.register(EncounterReason, EncounterReasonAdmin)
