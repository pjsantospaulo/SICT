# Generated by Django 3.0.2 on 2020-03-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200227_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='creatinina',
            field=models.TextField(verbose_name='Creatinina'),
        ),
    ]
