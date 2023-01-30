# Generated by Django 4.0.4 on 2022-05-01 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('InventoryManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.SmallIntegerField(choices=[(99, 'super user'), (50, 'warehouse admin'), (30, 'sales person'), (10, 'store manager')])),
            ],
        ),
        migrations.CreateModel(
            name='SalesManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isGolden', models.BooleanField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='InventoryManagement.store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='PeopleManagement.user')),
            ],
        ),
    ]