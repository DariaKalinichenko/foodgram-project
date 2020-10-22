from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.utils import json

from recipe.models import Recipe, FollowRecipe


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
        recipe.delete()
        return JsonResponse({"success": True})
