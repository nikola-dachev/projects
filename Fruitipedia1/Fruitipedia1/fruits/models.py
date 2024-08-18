from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia1.fruits.validators import validate_fruit


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name  = models.CharField(max_length=30,
                             validators=[MinLengthValidator(2), validate_fruit]
                             )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'fruits')