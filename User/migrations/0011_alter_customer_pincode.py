# Generated by Django 5.1 on 2024-09-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]