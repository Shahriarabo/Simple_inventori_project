# Generated by Django 5.0.2 on 2024-02-18 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_unit_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('purchace_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vendor')),
            ],
            options={
                'verbose_name_plural': 'Purchaces',
            },
        ),
    ]
