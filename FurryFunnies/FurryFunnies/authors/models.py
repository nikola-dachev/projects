from django.core.validators import MinLengthValidator
from django.db import models

from FurryFunnies.authors.validators import validate_name, validate_passcode


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=40,
                                  validators = [MinLengthValidator(4), validate_name])

    last_name = models.CharField(max_length=50,
                                 validators = [MinLengthValidator(2), validate_name])

    passcode = models.CharField(max_length=6,
                                 validators= [validate_passcode],
                                 help_text="Your passcode must be a combination of 6 digits")

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(null =True, blank = True)

    image_url = models.URLField(null = True, blank = True)

    def get_full_names(self):
        return f'{self.first_name} {self.last_name}'