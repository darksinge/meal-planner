from django import forms
from .models import Recipe, IngredientListItem, Ingredient


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']


class IngredientListItemForm(forms.ModelForm):
    class Meta:
        model = IngredientListItem
        fields = ['ingredient', 'amount', 'measurement']

    amount = forms.CharField(max_length=12, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Amount'}))

    ingredient = forms.CharField(max_length=255, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Ingredient'}))
