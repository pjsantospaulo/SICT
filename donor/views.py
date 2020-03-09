from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from donor.form.form import DonorForm
from donor.models import Donor


class DonorCreateView(CreateView):
    model = Donor
    form_class = DonorForm
    success_url = reverse_lazy('donor_list')


class DonorListView(ListView):
    model = Donor
    context_object_name = 'donor'

