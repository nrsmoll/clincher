from django.urls import include, path
from . import views

app_name = 'clinicalviewer'

urlpatterns = [
    # /ehr/
    path('', views.IndexView.as_view(), name='index'),
    #/ehr/<main_id>/
    path('clinicalviewer/view_patient/<int:pk>', views.DetailView.as_view(), name='detail'),
    #/ehr/main/add/
    path('clinicalviewer/new_patient/', views.MainCreate.as_view(), name='main-add'),
    #/ehr/main/2/
    path('clinicalviewer/update_patient/<int:pk>', views.MainUpdate.as_view(), name='main-update'),
    #/ehr/main/2/
    path('clinicalviewer/delete_patient/<int:pk>', views.MainDelete.as_view(), name='main-delete'),
    path('clinicalviewer/visit/add/', views.VisitCreate.as_view(), name='visit-add'),
]