# Generated by Django 3.0.1 on 2020-01-09 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('School', 'School'), ('Blood Bank', 'Blood Bank'), ('Parent', 'Parent'), ('Hospital', 'Hospital'), ('Teacher', 'Teacher'), ('Community', 'Community'), ('Driver', 'Driver'), ('Industry', 'Industry'), ('Hospital Staff', 'Hospital Staff')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tan', models.CharField(max_length=50)),
                ('gst', models.CharField(max_length=50)),
                ('opt_name', models.CharField(max_length=50)),
                ('desig', models.CharField(max_length=50)),
                ('mobile_number', models.BigIntegerField()),
                ('address', models.TextField()),
                ('teh', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]