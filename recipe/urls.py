from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("favorite/", views.favorite, name="favorite"),
    path("follow/", views.follow, name="follow"),

    path("<username>/follow", views.profile_follow, name="profile_follow"),
    path("<username>/unfollow", views.profile_unfollow, name="profile_unfollow"),
    path("new/", views.new_recipe, name="new_recipe"),
    # Профайл пользователя
    path("<username>/", views.profile, name="profile"),
    # Просмотр записи
    path("<username>/<int:recipe_id>/", views.recipe_view, name="recipe_view"),
    path("<username>/<int:recipe_id>/edit/", views.recipe_edit, name="recipe_edit"),


]

