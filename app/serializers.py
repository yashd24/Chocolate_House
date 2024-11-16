from .models import Flavors, Inventory, Customer_Suggestions
from rest_framework import serializers


class FlavorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavors
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Suggestions
        fields = '__all__'
