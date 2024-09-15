from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app.profiles.validators import validate_username


# Create your models here.
class Profile(models.Model):
    username= models.CharField(max_length=15,
                               validators=[MinLengthValidator(2), validate_username])
    email = models.EmailField()
    age = models.PositiveIntegerField()
