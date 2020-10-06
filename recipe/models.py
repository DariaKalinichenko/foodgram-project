from django.conf import settings
from django.db import models
from django.utils import timezone


class Ingredients(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    dimension = models.CharField(max_length=200)


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    text = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    tag = models.TextField()
    time = models.TimeField()
    slug = models.SlugField()

    def create(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



