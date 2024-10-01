from django.db import models
from .lomba import Lomba  

# Model Peserta Lomba
class Peserta(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    no_hp = models.CharField(max_length=13)
    alamat = models.CharField(max_length=255)
    lomba = models.ForeignKey(Lomba, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama