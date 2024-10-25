from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from TastyRecipes.profiles.models import Profile


# Create your models here.
class Recipe(models.Model):
    CUISINE_TYPE_CHOICES = (
        ("French", "French"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Balkan", "Balkan" ),
        ("Other", "Other"),

    )
    title = models.CharField(max_length=100,
                             unique= True,
                             validators = [MinLengthValidator(10)],
                             error_messages={
                                 'unique': "We already have a recipe with the same title!"}
                             )
    cuisine_type =models.CharField(max_length=7, choices= CUISINE_TYPE_CHOICES)

    ingredients = models.TextField(help_text="Ingredients must be separated by a comma and space.")

    instructions= models.TextField()

    cooking_time= models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
        validators = [MinValueValidator(1)]
    )

    image_url = models.URLField(null=True, blank=True)

    author = models.ForeignKey(Profile,
                               on_delete= models.CASCADE,
                               related_name = 'recipes',
                               editable= False)
