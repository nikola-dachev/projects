from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeed.profiles.validators import validate_username


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=15,
                                validators = [MinLengthValidator(3,"Username must be at least 3 chars long!"),
                                              validate_username]
                                )
    email = models.EmailField()
    age = models.IntegerField(help_text="Age requirement: 21 years and above.",
                              validators = [MinValueValidator(21)])
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)

    def get_names(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return ''