from django.contrib import admin
from django.contrib.auth.hashers import make_password  # Untuk hashing password
from .models.penyelenggara import Penyelenggara
from .models.account import Account
from .models.peserta import Peserta  
from .models.lomba import Lomba  
from .models.jurusan import Jurusan  

class PesertaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'no_hp', 'alamat', 'lomba')

    def save_model(self, request, obj, form, change):
        # Simpan peserta terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah user dengan email peserta sudah ada
        user, created = Account.objects.get_or_create(
            email=obj.email,  # Pastikan menggunakan email dari peserta
            defaults={
                'password': make_password('default_password'),  # Menggunakan hashing password
                'role': Account.PESERTA  # Atur role sebagai peserta
            }
        )

        if not created:
            # Jika user sudah ada, perbarui role (jika perlu)
            user.role = Account.PESERTA
            user.save()

class AdminLombaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'nomor_ponsel', 'alamat')

    def save_model(self, request, obj, form, change):
        # Simpan Admin Lomba terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah user dengan email Admin sudah ada
        user, created = Account.objects.get_or_create(
            email=obj.email,  # Pastikan menggunakan email dari admin
            defaults={
                'password': make_password('default_password'),  # Menggunakan hashing password
                'role': Account.ADMIN  # Atur role sebagai Admin Lomba
            }
        )

        if not created:
            # Jika user sudah ada, perbarui role (jika perlu)
            user.role = Account.ADMIN
            user.save()

class JurusanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'fakultas', 'lokasi')

class LombaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_lomba', 'tanggal', 'lokasi', 'jurusan')

# Daftarkan Peserta dengan custom PesertaAdmin
admin.site.register(Peserta, PesertaAdmin)
# Daftarkan Admin Lomba dengan custom AdminLombaAdmin
admin.site.register(Penyelenggara, AdminLombaAdmin)
# Daftarkan Model Jurusan dan Lomba
admin.site.register(Jurusan, JurusanAdmin)
admin.site.register(Lomba, LombaAdmin)
# Daftarkan Model Account jika belum didaftarkan
admin.site.register(Account)
