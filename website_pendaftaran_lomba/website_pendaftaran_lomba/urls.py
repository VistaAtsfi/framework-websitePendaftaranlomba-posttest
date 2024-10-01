from django.contrib import admin
from django.urls import path
from lomba import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Aktifkan akses ke Django admin
    path('', views.index, name='index'),
    path('daftar/', views.daftar_lomba, name='daftar_lomba'),
]
