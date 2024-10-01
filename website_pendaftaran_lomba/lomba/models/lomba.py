from django.db import models
from .jurusan import Jurusan  # Pastikan untuk mengimpor model Jurusan

# Model Lomba
class Lomba(models.Model):
    nama = models.CharField(max_length=255)
    jenis_lomba = models.CharField(max_length=100)
    tanggal = models.DateField()
    lokasi = models.CharField(max_length=255)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)  # Hubungkan dengan Jurusan

    def __str__(self):
        return self.nama
