from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    # metadata pinting the serilizing model
    class Meta: 
        model = Drink
        fields = ['id', 'name', 'description']
