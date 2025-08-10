from django.db import models

# Create your models here.

class FirstTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()  # Removed max_length
    phone = models.BigIntegerField()  # For large numbers like phone numbers
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name




class Cars(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()  # Removed max_length
    phone = models.BigIntegerField()  # For large numbers like phone numbers
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class user_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.BigIntegerField()
    password = models.CharField()