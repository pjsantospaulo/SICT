from django.db import models


class Hospital(models.Model):
    name = models.CharField("Hospital Notificante", max_length=150)
    bed = models.CharField("Leito", max_length=20)
    phone = models.CharField("Telefone", max_length=20)
    branch = models.CharField("Ramal", max_length=10)

    def __str__(self):
        return self.name
