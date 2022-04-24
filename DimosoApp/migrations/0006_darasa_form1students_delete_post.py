# Generated by Django 4.0.3 on 2022-04-11 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0005_form1report_delete_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Darasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('idadi', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form1Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/Form1Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.darasa')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]