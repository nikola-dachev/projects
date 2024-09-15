import re

from django.core.exceptions import ValidationError


def validate_username(username):
    pattern = r'^[A-Za-z0-9_]+$'
    if not re.fullmatch(pattern, username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def validate_username2(username2):
    if not all(char.isalnum() or char =='_' for char in username2):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")