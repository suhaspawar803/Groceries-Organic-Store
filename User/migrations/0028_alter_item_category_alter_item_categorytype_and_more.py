# Generated by Django 5.0.4 on 2024-10-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0027_alter_item_category_alter_item_categorytype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='categorytype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]