from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeed.cars.validators import validate_year
from WorldOfSpeed.profiles.models import Profile


# Create your models here.
class Car(models.Model):
    CAR_TYPE_CHOICES = (
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag" , "Drag"),
        ("Other", "Other")
    )

    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    model = models.CharField(max_length=15,
                             validators = [MinLengthValidator(1)]
                             )
    year = models.IntegerField(validators  = [validate_year])
    image_url = models.URLField(unique=True,
                                error_messages = {
                                    'unique': "This image URL is already in use! Provide a new one.",
                                },
                                )
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cars', editable =False)