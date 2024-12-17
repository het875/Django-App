from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email_id = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)  
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    block_expiration = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    unsuccessful_attempts = models.IntegerField(default=0)
    pass
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    is_deleted = models.BooleanField(default=False)  
    shop_id = models.IntegerField()  
    is_customisable = models.BooleanField(default=False)  
    attributes = models.JSONField()  # Store additional attributes as JSON data
    category = models.CharField(max_length=100)  
    label = models.CharField(max_length=100)  
    images = models.JSONField()  
    sizes = models.JSONField()  
    colours = models.JSONField() 
    fabric = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField()  
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)  
    preferred_amount = models.IntegerField()  
    preferred_age = models.CharField(max_length=50)  
    preferred_season = models.CharField(max_length=50)




