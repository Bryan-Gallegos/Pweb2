# Generated by Django 2.1.5 on 2020-07-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0002_auto_20200716_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=150)),
                ('specialty', models.CharField(max_length=50)),
                ('code', models.IntegerField(max_length=5)),
            ],
        ),
    ]
