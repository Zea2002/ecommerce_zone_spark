# Django imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, StockViewSet

# Defining the router
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'stocks', StockViewSet)

# Defining the urlpatterns for the product app and including the router
urlpatterns = [
    path('', include(router.urls)),
]