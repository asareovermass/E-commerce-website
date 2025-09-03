from django.db import models
import datetime


class Categroy(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    categroy = models.ForeignKey(Categroy, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, blank= True, null= True)
    image = models.ImageField(upload_to= 'uploads/product/')

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, default=1, on_delete=models.CASCADE)
    quatity = models.IntegerField(default=1)
    email = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=False)  
    date =  models.DateField(default=datetime.datetime.today) 

