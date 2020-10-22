from django.contrib import admin
from .models import Recipe, Ingredients, Tag, RecipeIngredient


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'title')
    inlines = (RecipeIngredientInline,)


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    list_filter = ('title',)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


admin.site.register(Tag, TagAdmin)

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Ingredients, IngredientsAdmin)

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)