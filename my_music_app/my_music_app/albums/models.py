from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profiles.models import Profile


# Create your models here.
class Album(models.Model):
    GENRE_CHOICES = (
        ("Pop Music","Pop Music"),
        ("Jazz Music","Jazz Music"),
        ( "R&B Music", "R&B Music"),
        ("Rock Music","Rock Music"),
        ("Country Music","Country Music"),
        ( "Dance Music", "Dance Music"),
        ( "Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    )

    album_name= models.CharField(max_length=30, unique = True)
    artist_name = models.CharField(max_length=30)
    genre= models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank = True, null = True)
    image_url = models.URLField()
    price = models.FloatField(validators= [MinValueValidator(0.0)])
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ='albums')
