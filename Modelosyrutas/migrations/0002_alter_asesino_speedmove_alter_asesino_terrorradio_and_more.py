# Generated by Django 5.1.1 on 2024-10-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelosyrutas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesino',
            name='speedmove',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='asesino',
            name='terrorradio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='asesino',
            name='usagerate',
            field=models.CharField(max_length=50),
        ),
    ]