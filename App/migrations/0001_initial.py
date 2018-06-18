# Generated by Django 2.0.2 on 2018-06-11 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('street_code', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Address')),
            ],
        ),
    ]