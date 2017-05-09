from django.db import models


class Famille(models.Model):
    famille = models.CharField(max_length = 100)

    def __str__(self):
        return self.famille


class Composition(models.Model):
    composition = models.CharField(max_length = 100)
    famille = models.ForeignKey(Famille, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.composition


class SousComposition(models.Model):
    souscomp = models.CharField(max_length = 100)
    composition = models.ForeignKey(Composition, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.souscomp


class Medicament(models.Model):
    nom = models.CharField(max_length = 100)
    dosage = models.CharField(max_length = 100, null = True, blank = True)
    forme = models.CharField(max_length = 100, null = True, blank = True)
    presentation = models.CharField(max_length = 100, null = True, blank = True)
    prescription = models.CharField(max_length = 300)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE, null=True, blank=True)
    composition = models.ForeignKey(Composition, on_delete = models.CASCADE, null = True, blank = True)
    souscomp = models.ForeignKey(SousComposition, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        if self.dosage:
            return self.nom + ' ' + self.dosage
        else:
            return self.nom