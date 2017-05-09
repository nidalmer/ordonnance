from django.views import generic
from .models import Famille, Composition, SousComposition, Medicament
from easy_pdf.views import PDFTemplateView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime



class IndexView(generic.ListView):
    template_name = 'meds/index.html'
    context_object_name = 'meds'
    model = Medicament

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'fams' : Famille.objects.all(),
        })
        return context

    def get_queryset(self):
        return Medicament.objects.all()


class DetailView(generic.DetailView):
    model = Medicament
    template_name = 'meds/detail.html'
    context_object_name = 'med'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


class PrescriptionView(PDFTemplateView):
    template_name = 'meds/prescription.html'
    context_object_name = 'meds'
    model = Medicament

    def get_queryset(self):
        ids = map(int, self.kwargs['selected'].split(","))
        return Medicament.objects.filter(id__in=ids)

    def get_context_data(self, **kwargs):
        ids = map(int, self.kwargs['selected'].split(","))
        context = super(PrescriptionView, self).get_context_data(pagesize="A5", title="Ordonnance", **kwargs)
        context.update({
            'name' : self.kwargs['name'],
            'note': self.kwargs['note'],
            'meds': Medicament.objects.filter(id__in=ids),
            'date': datetime.now()
        })
        return context


class MedicamentCreate(generic.CreateView):
    model = Medicament
    fields = ['nom', 'dosage', 'forme', 'presentation', 'prescription', 'famille', 'composition', 'souscomp']
    success_url = reverse_lazy('meds:index')

class SousCompositionCreate(generic.CreateView):
    model = SousComposition
    fields = ['souscomp', 'composition']
    success_url = reverse_lazy('meds:index')

class CompositionCreate(generic.CreateView):
    model = Composition
    fields = ['composition', 'famille']
    success_url = reverse_lazy('meds:index')

class FamilleCreate(generic.CreateView):
    model = Famille
    fields = ['famille']
    success_url = reverse_lazy('meds:index')

