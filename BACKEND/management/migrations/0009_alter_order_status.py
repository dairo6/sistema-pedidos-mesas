# Generated by Django 5.2.1 on 2025-06-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_salerecord_saleitemrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('confirmed', 'Confirmado'), ('preparing', 'En preparación'), ('ready_to_deliver', 'Listo para Entregar'), ('delivered', 'Entregado'), ('paid', 'Pagado'), ('annulled', 'Anulado')], default='pending', max_length=20),
        ),
    ]
