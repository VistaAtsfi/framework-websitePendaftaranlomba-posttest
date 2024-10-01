from django.db import models

class Account(models.Model):
    PESERTA = 1
    ADMIN = 2
    ROLE_CHOICES = (
        (PESERTA, 'Peserta'),
        (ADMIN, 'Admin Lomba'),
    )

    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)  # Panjang standar untuk password hash di Django
    role = models.IntegerField(choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"