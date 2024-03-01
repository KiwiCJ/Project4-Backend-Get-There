from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3) 
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    symbol_native = models.CharField(max_length=10)
    decimal_digits = models.IntegerField()

    def __str__(self):
        return self.code


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user_currency = models.CharField(max_length=100, blank=True, null=True)  
    country_currency = models.CharField(max_length=100, blank=True, null=True) 
    notes = models.TextField(blank=True, null=True)
    amount_needed = models.DecimalField(max_digits=10, decimal_places=2)
    amount_saved = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name