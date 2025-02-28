# qr_generator/models.py
from django.db import models

class QRCodeData(models.Model):
    unique_id = models.UUIDField(unique=True, editable=False)
    image_data = models.TextField()  # Store the base64 encoded image data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.unique_id)