from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipes.profiles.validators import validate_first_letter


# Create your models here.

class Profile(models.Model):
    nickname= models.CharField(max_length =20,
                               unique=True,
                               validators = [MinLengthValidator(2,"Nickname must be at least 2 chars long!")]
                               )
    first_name = models.CharField(max_length =30,
                                  validators = [validate_first_letter])

    last_name = models.CharField(max_length =30,
                                 validators = [validate_first_letter])

    chef = models.BooleanField(default=False)

    bio = models.TextField(null=True,blank=True)

    def get_names(self):
        return f"{self.first_name} {self.last_name}"
