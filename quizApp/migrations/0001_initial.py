# Generated by Django 2.2.7 on 2019-11-30 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='quizApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained', models.IntegerField()),
                ('total', models.IntegerField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Subject'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_a', models.CharField(max_length=50)),
                ('choice_b', models.CharField(max_length=50)),
                ('choice_c', models.CharField(max_length=50)),
                ('choice_d', models.CharField(max_length=50)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.Question')),
            ],
        ),
    ]
