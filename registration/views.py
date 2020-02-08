from django.shortcuts import render

from registration.form.form import RegistrationForm


def registration_new(request):
    form = RegistrationForm
    data = {"form": form}
    return render(request, 'registration.html', data)
