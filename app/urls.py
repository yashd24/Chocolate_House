from django.urls import path
from .views import FlavorsView, IngredientsView, SuggestionsView, index, inventory

urlpatterns = [
    path('', index, name='index'),
    path('flavors/', FlavorsView.as_view(), name='flavors'),
    path('flavors/<int:pk>/', FlavorsView.as_view(), name='flavors'),
    path('inventory/', IngredientsView.as_view(), name='ingredients'),
    path('inventory/<int:pk>/', IngredientsView.as_view(), name='ingredients'),
    path('suggestions/', SuggestionsView.as_view(), name='suggestions'),
    path('inventory-page/', inventory, name='inventory')
]
