from django.db import models
from accounts.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default='')
    created_by = models.ForeignKey(User, related_name='created_recipes', on_delete=models.SET_NULL, null=True,
                                   blank=True)
    favorited_by = models.ManyToManyField(User, related_name='favorites')
    ingredients = models.ManyToManyField(Ingredient, through='IngredientListItem')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class IngredientListItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.ingredient.name
