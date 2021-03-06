# Generated by Django 3.0.1 on 2020-01-05 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='notes/')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Module')),
            ],
        ),
    ]
