from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'title', 'image', 'description', 'ingredients', 'tags', 'cooking_time')