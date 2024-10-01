from django.db import models

# Model Jurusan yang Mengadakan Lomba
class Jurusan(models.Model):
    nama = models.CharField(max_length=255)
    fakultas = models.CharField(max_length=255)
    keterangan = models.TextField()
    lokasi = models.CharField(max_length=255)

    def __str__(self):
        return self.nama