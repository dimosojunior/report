# Generated by Django 4.0.3 on 2022-04-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0003_report_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True),
        ),
    ]