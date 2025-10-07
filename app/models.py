from django.db import models

# Create your models here.

from django.db import models

class Dress(models.Model):
    brand_name = models.CharField(max_length=100)
    dress_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand_name} - {self.dress_type}"


class DressImage(models.Model):
    dress = models.ForeignKey(Dress, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dresses/')
    
    
    


class Lace(models.Model):
    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=6, decimal_places=2, help_text="Length in meters")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='laces/', blank=True, null=True)
    status = models.CharField(max_length=50)  # e.g., "Available", "Out of Stock"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    