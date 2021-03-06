from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .forms import CreateRecipeForm, IngredientListItemForm
from .models import Recipe, Ingredient, IngredientListItem
from django.shortcuts import reverse


class RecipeListView(ListView):
    template_name = 'recipes/recipe-list.html'
    model = Recipe

    def get_queryset(self):
        if 'user' in self.kwargs:
            return Recipe.objects.filter(created_by=self.kwargs['user'])
        return Recipe.objects.all()


class RecipeView(DetailView):
    template_name = 'recipes/recipe.html'
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.get(id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        return Recipe.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecipeCreateView(CreateView):
    form_class = CreateRecipeForm
    template_name = 'recipes/recipe-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inglist_form_url'] = reverse('recipes:ingredientList.create')
        return context


class IngredientListItemCreateView(CreateView):
    template_name = 'recipes/ingredient-list-item.html'
    model = IngredientListItem
    form_class = IngredientListItemForm

    # def get(self, request, *args, **kwargs):


