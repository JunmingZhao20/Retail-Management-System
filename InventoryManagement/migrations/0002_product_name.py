# Generated by Django 4.0.4 on 2022-05-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='apple', max_length=50),
            preserve_default=False,
        ),
    ]
