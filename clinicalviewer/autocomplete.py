from dal import autocomplete

from clinicalviewer.models import EncounterReason


class EncounterReasonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return EncounterReason.objects.none()

        qs = EncounterReason.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs