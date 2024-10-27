from django.core.validators import MinLengthValidator
from django.db import models

from FurryFunnies.authors.models import Author


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,
                             unique=True,
                             validators = [MinLengthValidator(5)],
                             error_messages={
                                 'unique': "Oops! That title is already taken. How about something fresh and fun?"
                             }
                             )

    image_url = models.URLField(help_text="Share your funniest furry photo URL!")

    content = models.TextField()

    updated_at = models.DateTimeField(auto_now=True, editable = False)

    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               editable = False,
                               related_name='posts')