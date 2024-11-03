# Generated by Django 5.1.1 on 2024-11-03 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelosyrutas', '0009_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superviviente',
            name='dlc',
        ),
        migrations.RemoveField(
            model_name='superviviente',
            name='perks',
        ),
        migrations.AddField(
            model_name='superviviente',
            name='usagerate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='superviviente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='superviviente',
            name='imageUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]