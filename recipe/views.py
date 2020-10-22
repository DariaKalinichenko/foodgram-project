from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from recipe.forms import RecipeForm
from recipe.models import Recipe, Ingredients, FollowUser
from django.core.paginator import Paginator


def index(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)
    return render(request, "index.html", {"recipes": recipes, 'page': page, 'paginator': paginator,})

@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new_recipe.html', {'form': form})
    form = RecipeForm()
    return render(request, 'new_recipe.html', {'form': form})

def recipe_view(request, recipe_id, username):

    recipe = get_object_or_404(Recipe, id=recipe_id)
    username = get_object_or_404(User, username=username)

    return render(request, 'singlePage.html',
        {'username': username, 'recipe': recipe, })

def recipe_edit(request):
    pass

def profile(request, username):
    username = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=username).select_related('author').all()
    paginator = Paginator(recipes, 6)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)

    if request.user.is_authenticated:
        following = FollowUser.objects.filter(user=request.user).filter(author=username).select_related('author')
        if not following:
            following = None
        else:
            following = True
        return render(request, "authorRecipe.html", {'username': username, 'page': page, 'paginator': paginator, 'following': following})
    return render(request, "authorRecipe.html", {'username': username, 'page': page, 'paginator': paginator, })


def favorite(request):
    follows = FollowUser.objects.filter(user=request.user).values('author')
    following_list = Recipe.objects.filter(author_id__in=follows).select_related('author')
    paginator = Paginator(following_list, 6)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(request, 'favorite.html', {'page': page, 'paginator': paginator})


def follow(request):
    follows = FollowUser.objects.filter(user=request.user).values('author')
    following_list = Recipe.objects.filter(author_id__in=follows).select_related('author')
    paginator = Paginator(following_list, 6)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(request, 'follow.html', {'page': page, 'paginator': paginator})


def profile_follow(request):
    pass


def profile_unfollow(request):
    pass



def page_not_found(request, exception):

    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользователской страницы 404 мы не станем

    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)