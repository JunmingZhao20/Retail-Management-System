# Generated by Django 4.0.4 on 2022-05-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesprice',
            name='purchase_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salesrecord',
            name='totalPrice',
            field=models.FloatField(),
        ),
    ]
