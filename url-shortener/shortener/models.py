from django.db import models
import uuid


class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_id = models.CharField(
        max_length=10, unique=True, default=uuid.uuid4().hex[:6]
    )

    def __str__(self):
        return f"{self.original_url} -> {self.short_id}"
