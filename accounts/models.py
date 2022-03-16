from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=100)
    loan_limit = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)


class Business(models.Model):
    business_name = models.CharField(max_length=100)

class Loan(models.Model):
    amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    loan_ref = models.CharField(max_length=100)
    borrower = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    principle = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    


