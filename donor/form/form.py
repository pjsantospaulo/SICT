from django.forms import ModelForm

from donor.models import Donor


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
