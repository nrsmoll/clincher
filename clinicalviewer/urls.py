from django.urls import include, path
from . import views

app_name = 'clinicalviewer'

urlpatterns = [
    # /ehr/
    path('', views.IndexView.as_view(), name='index'),
    path('clinicalviewer/home/', views.ProfileView.as_view(), name='home'),
    #/ehr/<profile_id>/
    path('clinicalviewer/view_patient/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
    #/ehr/profile/add/
    path('clinicalviewer/new_patient/', views.ProfileCreate.as_view(), name='profile-add'),
    #/ehr/profile/2/
    path('clinicalviewer/update_patient/<int:pk>', views.ProfileUpdate.as_view(), name='profile-update'),
    #/ehr/profile/2/
    path('clinicalviewer/delete_patient/<int:pk>', views.ProfileDelete.as_view(), name='profile-delete'),
    path('clinicalviewer/visit/add/<int:pk>/', views.VisitCreate.as_view(), name='visit-form'),
    path('clinicalviewer/visit/detail/<int:pk>/', views.VisitDetail.as_view(), name='visit-detail'),
    path('clinicalviewer/visit/delete/<int:pk>/', views.VisitDelete.as_view(), name='visit-delete'),
]