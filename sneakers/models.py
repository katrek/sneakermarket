from django.db import models
from django.conf import settings
from django.urls import reverse


class Brand(models.Model):
    brand_name = models.CharField(max_length=64, verbose_name='Brand')

    def __str__(self):
        return self.brand_name


class Sneakers(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200, verbose_name='Model name')
    model_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
    model_price = models.IntegerField()
    model_photo = models.ImageField(upload_to='photos/')


    def __str__(self):
        return self.model_name

    def get_absolute_url(self):
        return reverse('sneaker-details', args=[str(self.pk)])

