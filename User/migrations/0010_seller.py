# Generated by Django 5.1 on 2024-09-02 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_rename_costomer_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=50)),
                ('shop_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('Gst', models.CharField(max_length=50)),
                ('seller_code', models.CharField(max_length=50)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.customer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.usermaster')),
            ],
        ),
    ]
