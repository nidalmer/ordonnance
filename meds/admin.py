from django.contrib import admin
from .models import Famille, Composition, SousComposition, Medicament


admin.site.register(Famille)
admin.site.register(Composition)
admin.site.register(SousComposition)
admin.site.register(Medicament)
