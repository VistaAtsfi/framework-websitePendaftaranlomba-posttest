from django.contrib import admin
from django.urls import path
from lomba import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Aktifkan akses ke Django admin
    path('', views.index, name='index'),  # Homepage
    path('daftar/', views.daftar_lomba, name='daftar_lomba'),  # Formulir Pendaftaran Lomba
    path('lomba/', views.lomba_index, name='lomba_index'),  # Read (List Lomba)
    path('lomba/create/', views.lomba_create, name='lomba_create'),  # Create Lomba Baru
    path('lomba/update/<int:lomba_id>/', views.lomba_update, name='lomba_update'),  # Update Lomba
    path('lomba/delete/<int:lomba_id>/', views.lomba_delete, name='lomba_delete'),  # Delete Lomba
]
