from django import forms
from .models import Peliharaan, Gambar


class PeliharaanForm(forms.ModelForm):
    class Meta:
        model = Peliharaan
        fields = ('nama', )


class GambarForm(forms.ModelForm):
    class Meta:
        model = Gambar
        fields = ('gambar', )
