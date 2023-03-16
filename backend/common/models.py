from django.db import models
from django.core.validators import MinLengthValidator
from backend.models import BaseModel


class Place(BaseModel):
    """
    For tutors and students - what form of tutoring do they allow
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Disabled(BaseModel):
    """
    To highlight skills for teaching
    people with disabilities such
    as Braille language skill
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BaseComment(BaseModel):
    content = models.TextField(max_length=1024, validators=[MinLengthValidator(5)])


class BaseStar(BaseModel):
    CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]

    stars = models.CharField(max_length=1, choices=CHOICES, default=1)

    def __str__(self):
        return self.stars
