from django.contrib import messages
from django.shortcuts import render, redirect
from .models.peserta import Peserta

def index(request):
    return render(request, 'homepage/index.html')

def daftar_lomba(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        lomba = request.POST.get('lomba')
        
        # Simpan data ke database
        # peserta = PesertaLomba(nama=nama, email=email, lomba=lomba)
        # peserta.save()
        
         # Pesan sukses
        messages.success(request, 'Pendaftaran berhasil! Terima kasih telah mendaftar.')

        return redirect('index')  # Redirect ke halaman beranda setelah pendaftaran
    return render(request, 'homepage/daftar.html')

