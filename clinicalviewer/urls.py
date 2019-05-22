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
    path('clinicalviewer/visit/add/<int:pk>/', views.VisitCreate.as_view(), name='visit-form'),
    path('clinicalviewer/visit/detail/<int:pk>/', views.VisitDetail.as_view(), name='visit-detail'),
    path('clinicalviewer/visit/delete/<int:pk>/', views.VisitDelete.as_view(), name='visit-delete'),
]