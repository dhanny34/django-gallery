from django.contrib import admin
from .models import Peliharaan, Gambar


# Register your models here.
class GambarInline(admin.TabularInline):
    model = Gambar


@admin.register(Peliharaan)
class PeliharaanAdmin(admin.ModelAdmin):
    inlines = [
        GambarInline
    ]
