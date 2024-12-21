# Django imports
from django.shortcuts import render
from .models import Product, Category, Stock
from .serializers import ProductSerializer, CategorySerializer, StockSerializer
from rest_framework import viewsets, permissions,filters

# all the views are created here

#product viewset all logic is written here
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category','price','description'] #search fields
    ordering_fields = ['price']
    ordering = ['price'] #ordering by price
    filter_fields = ['category'] #filtering by category
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #permission for the user only authenticated user can modify the data but read only for others

#category viewset all logic is written here
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description'] #search fields
    ordering_fields = ['name']
    ordering = ['name'] #ordering by name
    filter_fields = ['name'] #filtering by name
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #permission for the user only authenticated user can modify the data but read only for others


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'quantity'] #search fields
    ordering_fields = ['product'] #ordering fields
    ordering = ['product'] #ordering by product
    filter_fields = ['product'] #filtering by product
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #permission for the user only authenticated user can modify the data but read only for others

