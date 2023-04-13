from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(unique=True, max_length=11)


class Account(models.Model):
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.account_number}  {self.bank_name}'


class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.account.account_number


class Wallet(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    beneficiary = models.ForeignKey('Beneficiary', on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)


class Beneficiary(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)


class Card(models.Model):
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=25)
    cvv = models.CharField(max_length=3)
    expiry_date = models.DateTimeField()
