from django.urls import path

from django.urls import path

from .views import RecipeView, RecipeCreateView, RecipeListView

app_name = 'recipes'
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes'),
    path('<int:user>', RecipeListView.as_view(), name='recipes.owned'),
    path('<int:pk>', RecipeView.as_view(), name='recipe'),
    path('create', RecipeCreateView.as_view(), name='recipe.create')
]
