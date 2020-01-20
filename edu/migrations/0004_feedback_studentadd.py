# Generated by Django 3.0.1 on 2020-01-08 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
        ('account', '0003_driver_com_id'),
        ('edu', '0003_schoolactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('aadhar', models.BigIntegerField()),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.BooleanField()),
                ('field2', models.BooleanField()),
                ('field3', models.BooleanField()),
                ('field4', models.BooleanField()),
                ('field5', models.BooleanField()),
                ('field6', models.BooleanField()),
                ('field7', models.BooleanField()),
                ('field8', models.BooleanField()),
                ('field9', models.BooleanField()),
                ('field10', models.BooleanField()),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Parent')),
                ('school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.School')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Student')),
                ('teacher_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Teacher')),
            ],
        ),
    ]