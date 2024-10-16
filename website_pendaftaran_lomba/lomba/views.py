from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models.lomba import Lomba
from .forms import LombaForm
from .models.peserta import Peserta
from django.views.decorators.http import require_POST

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

# READ Lomba
def lomba_index(request):
    query = request.GET.get('q')
    lombas = Lomba.objects.all()
    if query:
        lombas = Lomba.objects.filter(
            Q(nama__icontains=query) |
            Q(jenis_lomba__icontains=query) |
            Q(lokasi__icontains=query)
        )
    return render(request, 'lomba/index.html', {'lombas': lombas, 'query': query})

# CREATE Lomba
def lomba_create(request):
    if request.method == 'POST':
        form = LombaForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data lomba ke database
            messages.success(request, 'Lomba berhasil dibuat!')  # Pesan sukses
            return redirect('lomba_index')  # Redirect ke halaman index lomba
    else:
        form = LombaForm()
    return render(request, 'lomba/create.html', {'form': form})

# UPDATE Lomba
def lomba_update(request, lomba_id):
    lomba = get_object_or_404(Lomba, id=lomba_id)
    if request.method == 'POST':
        form = LombaForm(request.POST, instance=lomba)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data lomba berhasil diubah!')
            return redirect('lomba_index')
    else:
        form = LombaForm(instance=lomba)
    return render(request, 'lomba/update.html', {'form': form, 'lomba': lomba})

# DELETE Lomba
@require_POST
def lomba_delete(request, lomba_id):
    lomba = get_object_or_404(Lomba, id=lomba_id)
    lomba.delete()
    messages.success(request, 'Data lomba berhasil dihapus')
    return JsonResponse({'success': True})

