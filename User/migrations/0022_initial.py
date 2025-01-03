# Generated by Django 5.0.4 on 2024-09-12 05:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0021_remove_customer_user_id_remove_seller_customer_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('categorytype', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='SellerItem/')),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_verify', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100)),
                ('shop_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('gst', models.IntegerField(default=0)),
                ('seller_code', models.CharField(max_length=100, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.customer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.usermaster')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.usermaster'),
        ),
    ]
