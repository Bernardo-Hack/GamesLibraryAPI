# Generated by Django 5.1.2 on 2024-11-11 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('onWindows', models.BooleanField()),
                ('onMac', models.BooleanField()),
                ('onLinux', models.BooleanField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Games.publisher')),
            ],
        ),
    ]
