from django.conf.urls import url
from . import views

app_name = 'acrrmlogbook'

urlpatterns = [
    # /logbook/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/logbook/<main_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/logbook/main/add/
    url(r'main/add/$', views.MainCreate.as_view(), name='main-add'),
    #/logbook/main/2/
    url(r'^(?P<pk>[0-9]+)/$', views.MainUpdate.as_view(), name='main-update'),
    #/logbook/main/2/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.MainDelete.as_view(), name='main-delete'),

    url(r'visit/add/$', views.VisitCreate.as_view(), name='visit-add'),
]