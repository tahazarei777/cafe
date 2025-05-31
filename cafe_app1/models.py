from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField( max_length=50,unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category,related_name="products", on_delete=models.CASCADE,default=1)
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to='upload/product/',unique=True)

    def __str__(self):
        return self.name
    

