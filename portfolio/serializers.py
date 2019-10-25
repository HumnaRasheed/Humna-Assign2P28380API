from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
            model = Customer
            fields = ('name', 'address', 'customer_number', 'city', 'state', 'zip_code', 'email', 'email', 'cell_phone')
