# Generated by Django 4.1.3 on 2022-11-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_clientes_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacciones',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, default='2022-11-19'),
            preserve_default=False,
        ),
    ]
