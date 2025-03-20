from typing import __all__
from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  
        fields = ['Title', 'Price', 'Inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  
        fields = __all__