from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from registration.form.form import RegistrationForm
from registration.models import Registration


class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    success_url = reverse_lazy('registration_list')


class RegistrationListView(ListView):
    model = Registration
    context_object_name = 'registration'
