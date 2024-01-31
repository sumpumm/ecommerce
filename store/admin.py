from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    list_per_page=10
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity','discounted_price','category',)
    list_filter=('category',)
    search_fields=('name',)
    list_per_page=5
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('f_name','m_name','l_name','address','gender',)
    search_fields=('f_name',)
    list_per_page=10
 
 
class CartItemInline(admin.TabularInline):
    model = CartItem
    
 
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('customer',)
    inlines=(CartItemInline,)
    
 
# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display=('product','quantity',)
#     list_editable=('quantity',)
    

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display=('product','price','quantity','status',)
    
class OrderItemInline(admin.TabularInline):
     model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','status','payment_status','shipping_address',)
    inlines=(OrderItemInline,)
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('customer','product','star',)
    



    

    

    

    



