from django.shortcuts import render
from django.http import HttpResponse

from hospital.form.form import HospitalForm


def hospital_new(request):
    form = HospitalForm()
    data = {"form": form}
    return render(request, 'hospital.html', data)
