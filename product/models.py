from django.db import models

# Create your models here.
class Category(models.Model):          #category model
    # all category fields
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name #return category name

class Stock(models.Model):              #stock model
    # all stock fields
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name #return product name
#product model    
class Product(models.Model):
    # all product fields
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to='product_images', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name #return product name