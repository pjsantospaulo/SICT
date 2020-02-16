from django.db import models

from hospital.models import Hospital


class Donor(models.Model):
    name = models.CharField("Nome", max_length=200)
    birth_date = models.DateField("Data de  Nascimento")
    age = models.IntegerField("Idade")
    weight = models.CharField("Altura", max_length=10)
    sex = models.CharField("Sexo", max_length=30)
    color = models.CharField("Cor", max_length=30)
    rg = models.CharField("RG", max_length=20)
    cpf = models.CharField("CPF", max_length=20)
    cns = models.CharField("Cartão SUS", max_length=40)
    g_abo = models.CharField("G-ABO", max_length=20)
    mother_name = models.CharField("Nome Mão", max_length=155)
    death = models.DateTimeField()
    hospital = models.OneToOneField(Hospital, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
