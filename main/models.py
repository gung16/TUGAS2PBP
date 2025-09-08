import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = []
    
    name = models.CharField(max_length=100)  # nama item
    price = models.IntegerField()  # harga item
    description = models.TextField()  # deskripsi item
    thumbnail = models.URLField()  # link gambar item
    category = models.CharField(max_length=50)  # kategori item
    is_featured = models.BooleanField(default=False)  # status unggulan item
    rating = models.FloatField(default=0.0)  # rating produk
    weight = models.IntegerField()  # berat produk (kg atau gram)
    brand = models.CharField(max_length=100)  # merek produk
    
    def __str__(self):
        return self.title
    