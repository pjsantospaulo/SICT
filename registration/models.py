from django.db import models

from registration import const


class Registration(models.Model):

    rb = models.CharField(
        choices=const.RADIO,
        max_length=10,
        verbose_name='AVD'
          )

    # avd = models.BooleanField("AVD")
    tce = models.BooleanField("TCE")
    hsa = models.BooleanField("HSA")
    aveh = models.BooleanField("AVEH")
    enc_anoxica = models.BooleanField("Encefalopatia anoxica")
    others = models.TextField("Outros", max_length=189)
    historic = models.TextField("Historico")
    ureia = models.BooleanField("uréia")
    creatinina = models.BooleanField("Creatinina")
    donor_diabete = models.BooleanField("Diabetes no Doador")
    relatives = models.BooleanField("Em Parentes 1º Grau")
    hypertension = models.BooleanField("Hipertensão")
    cardiopathy = models.BooleanField("Cardiopatica")
    dst = models.BooleanField("DST")
    alcolismo = models.BooleanField("Alcolismo", default=False)
    drogas_ilicita = models.BooleanField("Drogras ilícitas", default=False)
    cirurgia_previa = models.BooleanField("Cirurgia prévia", default=False)
    intubado_desde = models.DateField("Intubado desde:")
    fio = models.CharField("FiO%", max_length=100)
    peep = models.CharField("PEEP", max_length=100)
    m_ventilado = models.CharField("Mod.Ventilado", max_length=100)
    complacencia = models.CharField("Complacência", max_length=100)
    receb_sangue = models.BooleanField("Recebeu Sangue")
    #se recebeu sangue a informa a data que recebeu
    dt_rs = models.DateField()
    tp_sangue = models.CharField("Tipo", max_length=4)
    vol_total = models.CharField("Vol.Total", max_length=8)
    dt_rs2 = models.DateField()
    tp_sangue2 = models.CharField("Tipo", max_length=4)
    vol_total2 = models.CharField("Vol.Total", max_length=8)
    dt_rs3 = models.DateField()
    tp_sangue3 = models.CharField("Tipo", max_length=4)
    vol_total3 = models.CharField("Vol.Total", max_length=8)
    # Drogas Vasoativas
    d_vasoativa = models.BooleanField()
    nora_vazao = models.CharField("Nora Vazão", max_length=4)
    concentracao_nora = models.CharField("Concentração", max_length=20)
    vasopressina = models.CharField("Vasopressina-Vazão", max_length=20)
    concentracao_vas = models.CharField("Concentração", max_length=20)
    vazao_vasopressina = models.CharField("Vazão", max_length=20)
    concentracao_vaz = models.CharField("Concentração", max_length=20)
    # Infecção
    infeccao = models.BooleanField()
    local_infec = models.CharField("Local", max_length=30)
    antibiotico1 = models.CharField("Antibiótico1", max_length=40)
    antibiotico2 = models.CharField("Antibiótico2", max_length=40)
    antibiotico3 = models.CharField("Antibiótico3", max_length=40)
    inicio1 = models.DateField()
    inicio2 = models.DateField()
    inicio3 = models.DateField()
    # Cultura positiva
    cultura_positiva = models.BooleanField()
    dt_cultura = models.DateField()
    local_cultura = models.CharField("Local Cultura", max_length=40)
    resultado_cultura = models.CharField("Resultado", max_length=30)
    # coleta de liquor
    coleta_liquor = models.BooleanField()
    dt_liquor = models.DateField()
    resultado_liquor = models.CharField("Resultado", max_length=40)
    # sorologias
    sifilis_nr = models.BooleanField("NR")
    sifilis_r = models.BooleanField("R")
    chagas_nr = models.BooleanField("Chagas NR")
    chagas_r = models.BooleanField("Chagas R")
    AgHBS_nr = models.BooleanField("AgHBS (Hep.B) NR")
    AgHBS_r = models.BooleanField("AgHBS (Hep.B) R")
    AntiHBS_nr = models.BooleanField("Anti-HBS (Hep.B) NR")
    AntiHBS_r = models.BooleanField("Anti-HBS (Hep.B) R")
    AntiHCV_nr = models.BooleanField("Anti-HCV (Hep.C) NR")
    AntiHCV_r = models.BooleanField("Anti-HCV (Hep.C) R")
    AntiHTLV_nr = models.BooleanField("Anti-HTLV NR")
    AntiHTLV_r = models.BooleanField("Anti-HTLV R")
    AntiHIV_nr = models.BooleanField("Anti-HIV NR")
    AntiHIV_r = models.BooleanField("Anti-HIV R")
    AntiHIV_nr1_2 = models.BooleanField("Anti-HIV 1 + 2 NR")
    AntiHIV_r1_2 = models.BooleanField("Anti-HIV 1 + 2 R")
    # termo de morte encefalica
    t_preenchido = models.BooleanField()
    p_gastrometria = models.BooleanField()
    familia_inf = models.BooleanField()
    # exames de imagem do abdômen
    exm_img = models.BooleanField()
    exm_img_tipo = models.BooleanField()
    data_preenche = models.DateField(auto_now_add=True)









