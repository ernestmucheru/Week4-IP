# Generated by Django 3.2.5 on 2021-07-27 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmergencyContact',
        ),
        migrations.AlterModelOptions(
            name='business',
            options={},
        ),
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={},
        ),
        migrations.AlterModelTable(
            name='business',
            table=None,
        ),
        migrations.AlterModelTable(
            name='neighbourhood',
            table=None,
        ),
    ]
