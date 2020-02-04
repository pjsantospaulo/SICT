from django.contrib import admin

from donor.models import Donor
from hospital.models import Hospital
from .form import RegistrationForm
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    form = RegistrationForm


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Hospital)
admin.site.register(Donor)
