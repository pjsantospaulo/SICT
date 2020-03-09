from django import forms

from registration.form import const
from registration.models import Registration


class RegistrationForm(forms.ModelForm):
    cause_ME = forms.CharField(widget=forms.RadioSelect(choices=const.cause_ME))
    donor_diabete = forms.CharField(widget=forms.RadioSelect(choices=const.donor_diabete))
    relatives = forms.CharField(widget=forms.RadioSelect(choices=const.relatives))
    hypertension = forms.CharField(widget=forms.RadioSelect(choices=const.hypertension))
    cardiopathy = forms.CharField(widget=forms.RadioSelect(choices=const.cardiopathy))
    dst = forms.CharField(widget=forms.RadioSelect(choices=const.dst))
    alcolismo = forms.CharField(widget=forms.RadioSelect(choices=const.alcolismo))
    drogas_ilicita = forms.CharField(widget=forms.RadioSelect(choices=const.drogas_ilicita))
    cirurgia_previa = forms.CharField(widget=forms.RadioSelect(choices=const.cirurgia_previa))
    receb_sangue = forms.CharField(widget=forms.RadioSelect(choices=const.receb_sangue))
    d_vasoativa = forms.CharField(widget=forms.RadioSelect(choices=const.d_vasoativa))
    infeccao = forms.CharField(widget=forms.RadioSelect(choices=const.infeccao))
    cultura_positiva = forms.CharField(widget=forms.RadioSelect(choices=const.cultura_positiva))
    coleta_liquor = forms.CharField(widget=forms.RadioSelect(choices=const.coleta_liquor))

    class Meta:
        model = Registration

        fields = ['cause_ME', 'donor_diabete', 'relatives', 'historic', 'donor',
                  'relatives', 'hypertension', 'cardiopathy', 'dst', 'alcolismo', 'drogas_ilicita',
                  'cirurgia_previa', 'receb_sangue', 'd_vasoativa', 'infeccao', 'cultura_positiva',
                  'coleta_liquor', 'ureia', 'creatinina'
                  ]
