from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    price=models.FloatField()
    discounted_price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    GENDER_CHOICES=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'OTHER')
    ]
    f_name=models.CharField(max_length=255,blank=True,null=True)
    m_name=models.CharField(max_length=255,blank=True,null=True)
    l_name=models.CharField(max_length=255,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True        
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    
    
class Order(models.Model):
    PENDING_CHOICE='P'
    CANCEL_CHOICE='C'
    COMPLETED_CHOICE='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICE,'PENDING'),
        (CANCEL_CHOICE,'CANCEL'),
        (COMPLETED_CHOICE,'COMPLETED'),
    ]
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status=models.CharField(choices=STATUS_CHOICES,default=PENDING_CHOICE,max_length=2)
    payment_status=models.BooleanField(default=False)
    shipping_address=models.CharField(max_length=255)
    
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    PENDING_CHOICE='P'
    CANCEL_CHOICE='C'
    COMPLETED_CHOICE='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICE,'PENDING'),
        (CANCEL_CHOICE,'CANCEL'),
        (COMPLETED_CHOICE,'COMPLETED'),
    ]
    status=models.CharField(choices=STATUS_CHOICES,default=PENDING_CHOICE,max_length=2)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    
        
class Review(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    star=models.IntegerField()