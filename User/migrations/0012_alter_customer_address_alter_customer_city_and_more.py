# Generated by Django 5.1 on 2024-09-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_customer_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='landmark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='Gst',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='shop_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]