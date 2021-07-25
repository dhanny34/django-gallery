from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Gambar, Peliharaan
from .forms import PeliharaanForm, GambarForm
from django.http import HttpResponseRedirect



def tambahpeliharaanview(request):
    # buat formset dulu
    # supaya bisa bekerja dengan beberapa form dalam satu template
    # extra 3 buat 3 gambar
    gambarformset = modelformset_factory(Gambar, form=GambarForm, extra=3)

    if request.method == 'GET':
        peliharaanform = PeliharaanForm()
        formset = gambarformset(queryset=Gambar.objects.none())

        return render(request, 'index.html', {'peliharaanform': peliharaanform, 'formset': formset})
    elif request.method == 'POST':
        peliharaanform = PeliharaanForm(request.POST)
        formset = gambarformset(request.POST, request.FILES)

        if peliharaanform.is_valid() and formset.is_valid():
            peliharaanobj = peliharaanform.save()

            for form in formset.cleaned_data:
                if form:
                    gambar = form['gambar']
                    Gambar.objects.create(gambar=gambar, peliharaan=peliharaanobj)
            return HttpResponseRedirect('/')
        else:
            print(peliharaanform.errors, formset.errors)


def galeriview(request, pk):
    peliharaan = Peliharaan.objects.get(id=pk)

    return render(request, 'galeri.html', {'peliharaan': peliharaan})