# Generated by Django 3.0.2 on 2020-01-21 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200109_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='school',
            new_name='school_id',
        ),
    ]
