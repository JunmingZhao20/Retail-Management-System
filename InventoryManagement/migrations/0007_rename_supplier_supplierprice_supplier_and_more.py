# Generated by Django 4.0.4 on 2022-05-02 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0006_remove_storeinventory_warehouseinventory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierprice',
            old_name='Supplier',
            new_name='supplier',
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='supplier',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='InventoryManagement.supplier'),
            preserve_default=False,
        ),
    ]
