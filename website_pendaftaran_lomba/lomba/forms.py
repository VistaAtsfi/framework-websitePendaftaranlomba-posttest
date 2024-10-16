from django import forms
from .models.lomba import Lomba

class LombaForm(forms.ModelForm):
    class Meta:
        model = Lomba
        fields = '__all__'  # Menggunakan semua field dari model Lomba
