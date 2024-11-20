from django.urls import path
from .views import FlavorsView, IngredientsView, SuggestionsView, index, inventory, customers_suggestions

urlpatterns = [
    path('', index, name='index'),
    path('flavors/', FlavorsView.as_view(), name='flavors'),
    path('flavors/<int:pk>/', FlavorsView.as_view(), name='flavors'),
    path('inventory/', IngredientsView.as_view(), name='ingredients'),
    path('inventory/<int:pk>/', IngredientsView.as_view(), name='ingredients'),
    path('suggestions/', customers_suggestions, name='suggestions'),
    path('inventory-page/', inventory, name='inventory'),

]
