# Generated by Django 5.1.1 on 2024-10-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelosyrutas', '0006_alter_habilidadasesino_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilidadsuperviviente',
            name='perks',
        ),
        migrations.AlterField(
            model_name='habilidadsuperviviente',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]