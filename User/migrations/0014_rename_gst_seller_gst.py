# Generated by Django 5.1 on 2024-09-05 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_alter_seller_gst'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='Gst',
            new_name='gst',
        ),
    ]