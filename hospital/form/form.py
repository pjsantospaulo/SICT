from django.forms import ModelForm

from hospital.models import Hospital


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital

        fields = "__all__"


