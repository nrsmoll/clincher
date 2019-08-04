from django.contrib import admin
from django.urls import include, path
from clinicalviewer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('clinicalviewer.urls')),
    path('encounterreason-autocomplete/', views.EncounterReasonAutocomplete.as_view(),
         name='encounterreason-autocomplete'),
]
