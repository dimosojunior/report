# Generated by Django 4.0.3 on 2022-04-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0015_reportissuestoparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportissuestoparent',
            name='combination',
        ),
        migrations.RemoveField(
            model_name='reportissuestoparent',
            name='darasa',
        ),
        migrations.RemoveField(
            model_name='reportissuestoparent',
            name='image',
        ),
        migrations.AddField(
            model_name='reportissuestoparent',
            name='email',
            field=models.EmailField(blank=True, default='@gmail.com', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='reportissuestoparent',
            name='phone',
            field=models.CharField(blank=True, default='+255', max_length=200, null=True),
        ),
    ]