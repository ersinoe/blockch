# Generated by Django 3.1.5 on 2021-01-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='secret_key',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='profile',
            name='trid',
            field=models.CharField(default='00000000000', max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
