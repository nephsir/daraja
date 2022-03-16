from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Loan
from mpesa_api.models import mpesa_response


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('__all__')

class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  mpesa_response
        fields = ('__all__')       