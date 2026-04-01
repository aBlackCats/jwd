from django.db import models

from django.db import models

class mahasiswa(models.Model):
    nim = models.CharField(max_length=12, unique=True)
    nama = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    profile = models.ImageField(upload_to='profile/', default='profile/default.jpg', null=True, blank=True)
    nomor = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.nama
