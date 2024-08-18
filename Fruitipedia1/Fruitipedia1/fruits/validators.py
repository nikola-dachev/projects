from django.core.exceptions import ValidationError


def validate_fruit(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")