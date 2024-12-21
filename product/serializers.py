from rest_framework import serializers
from .models import Product, Category, Stock

# product Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField() #source='category.name'
    class Meta:
        model = Product
        fields = '__all__'

# category Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# stock Serializers define the API representation.
class StockSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField(source='product.name') #source='product.name' when we want to display the name of the product
    class Meta:
        model = Stock
        fields = '__all__'
        

