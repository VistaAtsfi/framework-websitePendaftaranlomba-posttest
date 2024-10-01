from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Model Penyelenggara Lomba
class Penyelenggara(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    nomor_ponsel = models.CharField(max_length=15)
    alamat = models.TextField()

    def __str__(self):
        return self.nama