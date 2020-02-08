from django.shortcuts import render
from django.http import HttpResponse

from hospital.form.form import HospitalForm


def hospital_new(request):
    form = HospitalForm()
    data = {"form": form}
    return render(request, 'hospital.html', data)


def hospital_create(request):
    form = HospitalForm(request.POST or None, request.FILE or None)

    if form.is_valid():
        form.save()
    return render(request, 'hospital', {'form': form})

