# Generated by Django 5.0 on 2024-01-03 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='store.order'),
            preserve_default=False,
        ),
    ]