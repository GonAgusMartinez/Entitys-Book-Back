# Generated by Django 5.1.1 on 2024-10-16 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modelosyrutas', '0007_remove_habilidadsuperviviente_perks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidadsuperviviente',
            old_name='imagenUrl',
            new_name='imageUrl',
        ),
    ]
