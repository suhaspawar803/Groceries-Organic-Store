# Generated by Django 5.0.4 on 2024-09-12 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_alter_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
        migrations.DeleteModel(
            name='UserMaster',
        ),
    ]
