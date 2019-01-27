from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) # com charfield max_length é requerido
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default='this is cool') # se eu mudar aqui p/ blank=False e null=False e der migrations/ate, ele vai dar erro no browser, porque tinha deixado um campo em branco
    featured = models.BooleanField() # criei esse campo após a concepção do banco. para validá-lo nos casos anteriores: null=True, ou default=True
