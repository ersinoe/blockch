# Generated by Django 3.1.5 on 2021-01-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notechainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.CharField(default='2021-01-21 12:27:12', max_length=20),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_protected',
            field=models.CharField(default='2021-01-21 12:27:12', max_length=20),
        ),
    ]