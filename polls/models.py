from django.db import models

class Jurusan(models.Model):
    nama_jurusan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_jurusan

class Prodi(models.Model):
    nama_prodi = models.CharField(max_length=50)
    id_jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nama_prodi

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=12, unique=True)
    nama = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    profile = models.ImageField(upload_to='profile/', default='profile/default.jpg', null=True, blank=True)
    nomor = models.CharField(max_length=12, blank=True, null=True)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nama