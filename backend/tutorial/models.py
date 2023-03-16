from django.db import models
from django.db.models import Avg
from django.contrib.postgres.fields import DateRangeField
from django.core.validators import MinValueValidator
from backend.models import BaseModel
from common.models import BaseComment, Place, Disabled


class Language(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tutorial(BaseModel):
    """
    scope - what range of learning is guaranteed by tutoring ex. high school
    lvl - whether you are learning from scratch or whether some basic elements are needed?
    essential - if you need any basic elements, place them here
    """

    SCRATCH = "S"
    THRESHOLD = "T"

    KIND_CHOICES = [
        (SCRATCH, "FROM SCRATCH"),
        (THRESHOLD, "FROM THRESHOLD"),
    ]

    name = models.CharField(max_length=255)
    date = DateRangeField()
    price = models.PositiveIntegerField()
    people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    description = models.TextField()
    scope = models.TextField()
    lvl = models.CharField(choices=KIND_CHOICES, max_length=1)
    essential = models.TextField(max_length=1024, blank=True, null=True)
    learning_form = models.TextField(max_length=1024)
    homework = models.BooleanField()
    status = models.BooleanField()
    place = models.ManyToManyField(Place)
    support_disabled = models.ManyToManyField(Disabled, blank=True)
    language = models.ManyToManyField(Language)

    @staticmethod
    def get_avg_price():
        return Tutorial.objects.aggregate(Avg("price"))["price__avg"]

    def __str__(self):
        return self.name


class PremiumTutorial(BaseModel):
    status = models.BooleanField()
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

    def set_status(self):
        pass


class CommentTutorial(BaseComment):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
