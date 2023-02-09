from django.db import models
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
