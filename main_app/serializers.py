from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Trip, Currency


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        # fields = ['user','name', 'location', 'user_currency', 'country_currency', 'notes', 'amount_needed', 'amount_saved']
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'symbol', 'name', 'symbol_native', 'decimal_digits', 'rounding', 'name_plural']
