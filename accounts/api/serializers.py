from rest_framework import serializers
from accounts.models import Bank, Account


# Serializers define the API representation.
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'bank',
            'number',
            'name',
            'validity',
            'balance',
            'limit',
            'cvv',
            'active'
        ]