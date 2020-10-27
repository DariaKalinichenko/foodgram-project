from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.utils import json

from recipe.models import Recipe, FollowRecipe, Ingredients, FollowUser, ShoppingList


class Favorites(LoginRequiredMixin, View):
    """
    Функция добавления/удаления рецепта из "Избранное"
    """
    def post(self, request):
        req_ = json.loads(request.body)
        print(req_)
        recipe_id = req_.get("id", None)
        if recipe_id is not None:
            recipe = get_object_or_404(Recipe, id=recipe_id)
            print(recipe)
            obj, created = FollowRecipe.objects.get_or_create(
                user=request.user, recipe=recipe
            )
            if created:
                return JsonResponse({"success": True})
            return JsonResponse({"success": False})
        return JsonResponse({"success": False}, status=400)

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(
            FollowRecipe, recipe=recipe_id, user=request.user
        )
        print(recipe)
        recipe.delete()
        return JsonResponse({"success": True})


class Purchases(LoginRequiredMixin, View):

    def post(self, request):
        recipe_id = json.loads(request.body)['id']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        ShoppingList.objects.get_or_create(
            user=request.user, recipe=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = get_object_or_404(User, username=request.user.username)
        obj = get_object_or_404(ShoppingList, user=user, recipe=recipe)
        obj.delete()
        return JsonResponse({'success': True})


class Subscribe(LoginRequiredMixin, View):
    def post(self, request):
        req_ = json.loads(request.body)
        print(req_)
        author_id = req_.get("id", None)
        if author_id is not None:
            author = get_object_or_404(User, id=author_id)
            print(author)
            obj, created = FollowUser.objects.get_or_create(
                user=request.user, author=author
            )
            print(request.user)
            if created:
                return JsonResponse({"success": True})
            return JsonResponse({"success": False})
        return JsonResponse({"success": False}, status=400)

    def delete(self, request, author_id):
        user = get_object_or_404(
            User, username=request.user.username
        )
        author = get_object_or_404(User, id=author_id)
        obj = get_object_or_404(FollowUser, user=user, author=author)
        obj.delete()
        return JsonResponse({"success": True})


class Purchase(LoginRequiredMixin, View):
    def post(self, request):
        recipe_id = json.loads(request.body)["id"]
        recipe = get_object_or_404(Recipe, id=recipe_id)
        ShoppingList.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse({"success": True})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = get_object_or_404(User, username=request.user.username)
        obj = get_object_or_404(ShoppingList, user=user, recipe=recipe)
        obj.delete()
        return JsonResponse({"success": True})


class Ingredient(LoginRequiredMixin, View):
    def get(self, request):
        text = request.GET['query']
        print(text)

        ingredients = list(Ingredients.objects.filter(
            title__icontains=text).values('title', 'dimension'))
        print(ingredients)
        return JsonResponse(ingredients, safe=False)