# Generated by Django 2.0.2 on 2018-06-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.ManyToManyField(to='App.Address'),
        ),
    ]