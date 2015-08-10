from django.conf.urls import url

from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^new/$', views.new_patient, name='new_patient'),
    url(r'^visitors/$', views.visitors, name='visitors'),
    url(r'^pending/$', views.pending, name='pending'),
    url(r'^search/$', views.search_page, name='search_page'),
    url(r'^patient/$', views.patient, name='patient'),
    #Ajax calls
    url(r'^searchPatients/$',ajax.searchPatients,name="searchPatients"),
    url(r'^createPatient/$',ajax.createPatient,name="createPatient"),
    url(r'^createVisit/$',ajax.createVisit,name="createVisit"),
]