from django.contrib import admin

from .form import RegistrationForm
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    form = RegistrationForm


admin.site.register(Registration, RegistrationAdmin)
