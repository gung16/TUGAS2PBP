import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('racket', 'Racket'),
        ('shoes', 'Shoes'),
        ('accesories', 'Accesories'),
        ('bags', 'Bags'),
        ('balls', 'Balls'),
    ]    
    # Sesuai
    name = models.CharField(max_length=100)  # nama item, saved as carchar for fast accessing
    price = models.IntegerField()  # harga item
    description = models.TextField()  # deskripsi item, no limit so it can be less fast
    thumbnail = models.URLField()  # link gambar item
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)  # status unggulan item
    
    # Add ons
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.FloatField(default=0.0)  # rating produk
    weight = models.IntegerField(default=0)  # berat produk (kg atau gram)
    brand = models.CharField(max_length=100)  # merek produk
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()