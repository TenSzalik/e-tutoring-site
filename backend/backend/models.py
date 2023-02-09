from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """
    Every model should inherit BaseModel.
    It's important to track which user created each db record.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True
