from django.conf.urls import url
from . import views

app_name = 'meds'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='medicament'),
    url(r'medicament/add/$', views.MedicamentCreate.as_view(), name='med-add'),
    url(r'souscomp/add/$', views.SousCompositionCreate.as_view(), name='souscomp-add'),
    url(r'comp/add/$', views.CompositionCreate.as_view(), name='comp-add'),
    url(r'famille/add/$', views.FamilleCreate.as_view(), name='fam-add'),
    url(r'^prescription/(?P<selected>.*)/(?P<name>.*)/(?P<note>.*)$', views.PrescriptionView.as_view(), name='prescription'),
]