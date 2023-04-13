from djoser.serializers import serializers

from wallet.models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'bank_name', 'account_name', 'amount'
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'account'
            'amount'
            'date']
