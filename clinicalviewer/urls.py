from django.urls import path
from . import views

app_name = 'clinicalviewer'

urlpatterns = [
    # /ehr/
    path('', views.IndexView.as_view(), name='index'),
    path('clinicalviewer/home/', views.PatientView.as_view(), name='home'),
    #/ehr/<profile_id>/
    path('clinicalviewer/view_patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    #/ehr/profile/add/
    path('clinicalviewer/new_patient/', views.PatientCreate.as_view(), name='patient-add'),
    #/ehr/profile/2/
    path('clinicalviewer/update_patient/<int:pk>', views.PatientUpdate.as_view(), name='patient-update'),
    #/ehr/profile/2/
    path('clinicalviewer/delete_patient/<int:pk>', views.PatientDelete.as_view(), name='patient-delete'),
    path('clinicalviewer/encounter/add/<int:pk>/', views.EncounterCreate.as_view(), name='encounter-form'),
    path('clinicalviewer/encounter/detail/<int:pk>/', views.EncounterDetail.as_view(), name='encounter-detail'),
    path('clinicalviewer/encounter/delete/<int:pk>/', views.EncounterDelete.as_view(), name='encounter-delete'),
    path('clinicalviewer/pasthistory/add/<int:pk>/', views.PasthxCreate.as_view(), name='pasthx-form'),
    path('clinicalviewer/pasthistory/detail/<int:pk>/', views.PasthxDetail.as_view(), name='pasthx-detail'),
    path('clinicalviewer/pasthistory/delete/<int:pk>/', views.PasthxDelete.as_view(), name='pasthx-delete'),



]