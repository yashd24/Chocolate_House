from django.shortcuts import render
from rest_framework.views import APIView
from .models import Flavors, Inventory, Customer_Suggestions
from .serializers import FlavorsSerializer, IngredientsSerializer, SuggestionsSerializer
from rest_framework.response import Response
from rest_framework import status


class FlavorsView(APIView):
    def get(self, request):
        flavors = Flavors.objects.all()
        serializer = FlavorsSerializer(flavors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlavorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flavor = Flavors.objects.get(pk=pk)
        flavor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientsView(APIView):
    def get(self, request):
        ingredients = Inventory.objects.all()
        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        ingredient = Inventory.objects.get(pk=pk)
        serializer = IngredientsSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ingredient = Inventory.objects.get(pk=pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SuggestionsView(APIView):
    def get(self, request):
        suggestions = Customer_Suggestions.objects.all()
        serializer = SuggestionsSerializer(suggestions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuggestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'app/index.html')


def inventory(request):
    items = Inventory.objects.all()

    return render(request, 'app/inventory.html', {'items': items})


def customers_suggestions(request):
    customers = Customer_Suggestions.objects.all()

    return render(request, 'app/customers.html', {'customers': customers})
