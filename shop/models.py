from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    def get_product_picture_filename(self, filename):
        folder = "product_pictures/"
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extension = filename.split('.')[-1]
        return "{}product-picture-{}.{}".format(folder, time, extension)

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(default='default/product-picture.png', upload_to=get_product_picture_filename)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Order(models.Model):
    items = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.FloatField()
