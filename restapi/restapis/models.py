from django.db import models
# Create your models here.
class products(models.Model):
     name=models.CharField(max_length=30,default="productname")
     price=models.CharField(max_length=10,default="Rs.0")
     imgurl=models.URLField()

     def __str__(self):
        return self.name