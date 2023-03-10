# Generated by Django 3.0 on 2022-03-14 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('languages', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Trainer')),
            ],
        ),
    ]
