from django.db import models


# Create your models here.
class Peliharaan(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama


def upload_galeri_gambar(instance, filename):
    return f"gambar/{instance.peliharaan.nama}/galeri/{filename}"


class Gambar(models.Model):
    gambar = models.ImageField(upload_to=upload_galeri_gambar)
    peliharaan = models.ForeignKey(Peliharaan, on_delete=models.CASCADE, related_name='gambar')
