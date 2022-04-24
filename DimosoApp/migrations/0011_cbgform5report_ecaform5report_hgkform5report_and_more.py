# Generated by Django 4.0.3 on 2022-04-16 01:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0010_combination_pcbform5report_pcmform5report_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CbgForm5Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='+255', max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/CbgFormFive/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub1', models.CharField(blank=True, default='Mathematics', max_length=200, null=True)),
                ('sub2', models.CharField(blank=True, default='English', max_length=200, null=True)),
                ('sub3', models.CharField(blank=True, default='Kiswahili', max_length=200, null=True)),
                ('sub4', models.CharField(blank=True, default='Physics', max_length=200, null=True)),
                ('sub5', models.CharField(blank=True, default='Biology', max_length=200, null=True)),
                ('sub1_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub2_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub3_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub4_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub5_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('total_marks', models.IntegerField(blank=True, default=1000, null=True)),
                ('sub1_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub2_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub3_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub4_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub5_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('total_obtained', models.IntegerField(blank=True, default=800, null=True)),
                ('sub1_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub2_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub3_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub4_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub5_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub1_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub2_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub3_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub4_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub5_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('Overall_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='Qualified', max_length=200, null=True)),
                ('stu_pos', models.IntegerField(blank=True, null=True)),
                ('all_stu', models.IntegerField(blank=True, null=True)),
                ('teacher_sign', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EcaForm5Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='+255', max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/EcaFormFive/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub1', models.CharField(blank=True, default='Mathematics', max_length=200, null=True)),
                ('sub2', models.CharField(blank=True, default='English', max_length=200, null=True)),
                ('sub3', models.CharField(blank=True, default='Kiswahili', max_length=200, null=True)),
                ('sub4', models.CharField(blank=True, default='Physics', max_length=200, null=True)),
                ('sub5', models.CharField(blank=True, default='Biology', max_length=200, null=True)),
                ('sub1_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub2_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub3_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub4_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub5_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('total_marks', models.IntegerField(blank=True, default=1000, null=True)),
                ('sub1_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub2_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub3_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub4_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub5_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('total_obtained', models.IntegerField(blank=True, default=800, null=True)),
                ('sub1_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub2_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub3_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub4_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub5_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub1_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub2_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub3_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub4_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub5_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('Overall_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='Qualified', max_length=200, null=True)),
                ('stu_pos', models.IntegerField(blank=True, null=True)),
                ('all_stu', models.IntegerField(blank=True, null=True)),
                ('teacher_sign', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HgkForm5Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='+255', max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HgkFormFive/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub1', models.CharField(blank=True, default='Mathematics', max_length=200, null=True)),
                ('sub2', models.CharField(blank=True, default='English', max_length=200, null=True)),
                ('sub3', models.CharField(blank=True, default='Kiswahili', max_length=200, null=True)),
                ('sub4', models.CharField(blank=True, default='Physics', max_length=200, null=True)),
                ('sub5', models.CharField(blank=True, default='Biology', max_length=200, null=True)),
                ('sub1_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub2_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub3_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub4_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub5_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('total_marks', models.IntegerField(blank=True, default=1000, null=True)),
                ('sub1_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub2_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub3_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub4_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub5_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('total_obtained', models.IntegerField(blank=True, default=800, null=True)),
                ('sub1_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub2_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub3_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub4_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub5_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub1_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub2_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub3_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub4_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub5_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('Overall_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='Qualified', max_length=200, null=True)),
                ('stu_pos', models.IntegerField(blank=True, null=True)),
                ('all_stu', models.IntegerField(blank=True, null=True)),
                ('teacher_sign', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HglForm5Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='+255', max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HglFormFive/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub1', models.CharField(blank=True, default='Mathematics', max_length=200, null=True)),
                ('sub2', models.CharField(blank=True, default='English', max_length=200, null=True)),
                ('sub3', models.CharField(blank=True, default='Kiswahili', max_length=200, null=True)),
                ('sub4', models.CharField(blank=True, default='Physics', max_length=200, null=True)),
                ('sub5', models.CharField(blank=True, default='Biology', max_length=200, null=True)),
                ('sub1_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub2_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub3_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub4_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub5_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('total_marks', models.IntegerField(blank=True, default=1000, null=True)),
                ('sub1_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub2_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub3_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub4_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub5_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('total_obtained', models.IntegerField(blank=True, default=800, null=True)),
                ('sub1_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub2_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub3_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub4_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub5_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub1_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub2_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub3_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub4_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub5_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('Overall_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='Qualified', max_length=200, null=True)),
                ('stu_pos', models.IntegerField(blank=True, null=True)),
                ('all_stu', models.IntegerField(blank=True, null=True)),
                ('teacher_sign', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HklForm5Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='+255', max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021', max_length=1000, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HklFormFive/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sub1', models.CharField(blank=True, default='Mathematics', max_length=200, null=True)),
                ('sub2', models.CharField(blank=True, default='English', max_length=200, null=True)),
                ('sub3', models.CharField(blank=True, default='Kiswahili', max_length=200, null=True)),
                ('sub4', models.CharField(blank=True, default='Physics', max_length=200, null=True)),
                ('sub5', models.CharField(blank=True, default='Biology', max_length=200, null=True)),
                ('sub1_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub2_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub3_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub4_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('sub5_marks', models.IntegerField(blank=True, default=100, null=True)),
                ('total_marks', models.IntegerField(blank=True, default=1000, null=True)),
                ('sub1_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub2_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub3_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub4_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('sub5_obtained', models.IntegerField(blank=True, default=80, null=True)),
                ('total_obtained', models.IntegerField(blank=True, default=800, null=True)),
                ('sub1_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub2_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub3_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub4_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub5_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('sub1_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub2_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub3_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub4_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('sub5_remaks', models.CharField(blank=True, default='Very Good', max_length=200, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('Overall_grade', models.CharField(blank=True, default='A', max_length=200, null=True)),
                ('rank', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='Qualified', max_length=200, null=True)),
                ('stu_pos', models.IntegerField(blank=True, null=True)),
                ('all_stu', models.IntegerField(blank=True, null=True)),
                ('teacher_sign', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HklForm5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HklForm5Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
            ],
        ),
        migrations.CreateModel(
            name='HglForm5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HglForm5Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
            ],
        ),
        migrations.CreateModel(
            name='HgkForm5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/HgkForm5Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
            ],
        ),
        migrations.CreateModel(
            name='EcaForm5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/EcaForm5Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
            ],
        ),
        migrations.CreateModel(
            name='CbgForm5Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/CbgForm5Students/')),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.combination')),
            ],
        ),
    ]
