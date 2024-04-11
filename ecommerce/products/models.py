from django.db import models
from customers.models import Customer
# Create your models here.

class Product(models.Model) :
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Review(models.Model) :
    user  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()