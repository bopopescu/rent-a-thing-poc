from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from core.models import Transaction, Wallet


class WalletSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Wallet
        fields = ('id','last_update', 'balance')

    def create(self, validated_data):

        wallet = Wallet.objects.get(id=validated_data['id'])

        wallet.balance = validated_data['balance']

        wallet.save()

        return wallet


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Transaction
        fields = ('amount_paid','credits_purchased','price_per_credit', 'transaction_code', 'user')

    def create(self, validated_data):

        transaction = Transaction.objects.create(
            amount_paid=validated_data['amount_paid'],
            credits_purchased=validated_data['credits_purchased'],
            price_per_credit=validated_data['price_per_credit'],
            transaction_code=validated_data['transaction_code'],
            user=validated_data['user']
        )

        try:
            wallet = Wallet.objects.get(id=transaction.user)
        except:
            wallet = Wallet.objects.create(id=transaction.user, balance=0)

        wallet.balance += validated_data['credits_purchased']

        wallet.save()

        return transaction
