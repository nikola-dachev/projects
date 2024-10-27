

from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")




def validate_passcode(value):
    if not (value.isdigit() and len(value) == 6):
        raise ValidationError("Your passcode must be a combination of 6 digits")