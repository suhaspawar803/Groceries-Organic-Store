
from django.db import models
from django.utils import timezone
# Create your models here.
class UserMaster(models.Model):
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=100)  # Increase as needed
    email = models.EmailField(max_length=254)  # Already increased
    mobile_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)  # Increase as needed
    is_verify = models.BooleanField(default=False)
    is_created = models.DateTimeField(default=timezone.now)
    is_updated = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

class Customer(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    state = models.CharField(max_length=100)  # Increase as needed
    city = models.CharField(max_length=100)  # Increase as needed
    address = models.CharField(max_length=200)  # Increase as needed
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    landmark = models.CharField(max_length=100)  # Increase as needed
    pincode = models.IntegerField(default=0)

class Seller(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    seller_name = models.CharField(max_length=100)  # Increase as needed
    shop_name = models.CharField(max_length=100)  # Increase as needed
    address = models.CharField(max_length=200,null=True)  # Increase as needed
    gst = models.IntegerField(default=0)  # Increase as needed
    seller_code = models.CharField(max_length=100,null=True)  # Increase as needed





class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    categorytype = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='SellerItem/', blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)  # Add valid_until field if not already added
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


from django.contrib.auth.models import User
from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # ForeignKey to the User model
    # Other fields


        
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
