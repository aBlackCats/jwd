from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('ganti-password/', views.ganti_password, name='ganti_password'),
    path("mahasiswa", views.data_mahasiswa, name="mahasiswa"),
    path("prodi", views.data_prodi, name="prodi"),
    path("/tambah_prodi", views.create_prodi, name="tambah_prodi"),
    path("/edit_prodi<int:id>", views.edit_prodi, name="edit_prodi"),
    path("/hapus_prodi<int:id>", views.hapus_prodi, name="hapus_prodi"),
    path("jurusan", views.data_jurusan, name="jurusan"),
    path("/tambah_jurusan", views.create_jurusan, name="tambah_jurusan"),
    path("/edit_jurusan<int:id>", views.edit_jurusan, name="edit_jurusan"),
    path("/hapus_jurusan<int:id>", views.hapus_jurusan, name="hapus_jurusan"),
    path("/data_baru", views.create, name="create"),
    path("/edit_data/<int:id>", views.edit, name="edit"),
    path("/hapus_data/<int:id>", views.hapus, name="hapus"),
    path("logout/", views.logout_view, name="logout"),
]
