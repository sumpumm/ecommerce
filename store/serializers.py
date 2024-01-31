from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    total_product=serializers.IntegerField()
    class Meta:
        model = Category
        fields = ['id', 'name','total_product']
    
    # def get_total_product(self,category:Category):
    #     return category.products.count()
        
        
class ProductSerializer(serializers.ModelSerializer):
    price_with_tax=serializers.SerializerMethodField()
    category=CategorySerializer(read_only=True)
    
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category'
    )
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'discounted_price','price_with_tax','category_id','category']
        
    def get_price_with_tax(self,product:Product):
        return (product.discounted_price *0.13)+product.discounted_price
    
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"        