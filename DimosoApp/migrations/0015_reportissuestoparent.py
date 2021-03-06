# Generated by Django 4.0.3 on 2022-04-18 23:02

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0014_alter_pcbform6students_darasa'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportIssuesToParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('send_through_email', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('send_through_text', models.TextField(blank=True, default='NAME amepatikana na kosa la kuanzisha mgomo yeye pamoja na wanafunzi wenzake tarehe 20/4/2022 hivyo tunapenda kukutaarifu kupitia ofisi ya nidhamu shule ya secondary St.Dimoso kwamba mwanao amepewa suspension ya wiki mbili na pindi atakaporejea unaombwa kufika naye hapa shuleni, kwa taarifa zaidi wasiliana na mwalimu wa nidhamu shule ya secondary St. Dimoso.', null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/Form1Students/')),
                ('combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.darasa')),
            ],
        ),
    ]
