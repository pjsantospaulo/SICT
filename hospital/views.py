from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from hospital.form.form import HospitalForm
from hospital.models import Hospital


class HospitalCreateView(CreateView):
    model = Hospital
    form_class = HospitalForm
    success_url = reverse_lazy('hospital_list')


class HospitalListView(ListView):
    model = Hospital
    context_object_name = 'hospitais'



