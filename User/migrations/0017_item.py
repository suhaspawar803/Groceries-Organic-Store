# Generated by Django 5.1 on 2024-09-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_alter_seller_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Home & Furniture', 'Home & Furniture'), ('Appliances', 'Appliances'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Sports, Books & More', 'Sports, Books & More'), ('Grocery', 'Grocery')], max_length=50)),
                ('subcategory', models.CharField(max_length=255)),
                ('type_category', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='items/')),
            ],
        ),
    ]