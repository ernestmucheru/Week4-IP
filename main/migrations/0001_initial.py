# Generated by Django 3.2.5 on 2021-07-26 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'e_contacts',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='hood_images/')),
            ],
            options={
                'db_table': 'neighbourhoods',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'businesses',
                'ordering': ['-name'],
            },
        ),
    ]
