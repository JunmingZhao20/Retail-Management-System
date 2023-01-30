# Generated by Django 4.0.4 on 2022-05-02 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0002_product_name'),
        ('PeopleManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesmanager',
            name='store',
        ),
        migrations.AddField(
            model_name='user',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='InventoryManagement.store'),
            preserve_default=False,
        ),
    ]
