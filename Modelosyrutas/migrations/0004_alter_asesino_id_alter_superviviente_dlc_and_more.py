# Generated by Django 5.1.1 on 2024-10-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelosyrutas', '0003_alter_asesino_dlc_alter_asesino_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesino',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='superviviente',
            name='dlc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='superviviente',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='superviviente',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
