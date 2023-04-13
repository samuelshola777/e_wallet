from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from wallet.models import Account


# Create your views here.


class AccountViewSet(ModelViewSet):
    model = Account
    feild = [
        'bank_name',''
    ]
