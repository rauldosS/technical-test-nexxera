from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    function = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'account',
            'description',
            'date',
            'value',
            'function'
        ]

    def get_function(self,obj):
        return obj.get_function_display()

    # def to_representation(self, instance):
    #     data = super(TransactionSerializer, self).to_representation(instance)

    #     result_data = {"status" : 200,"message" : "Category List"}
    #     result_data["response"] = data

    #     return result_data