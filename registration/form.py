from django import forms

from registration import const
from registration.models import Registration


class RegistrationForm(forms.ModelForm):
    rb = forms.CharField(widget=forms.RadioSelect(choices=const.RADIO))

    class Meta:
        model = Registration
        fields = ['rb', 'others', 'historic', 'relatives', 'm_ventilado', 'complacencia', 'peep', 'fio']
