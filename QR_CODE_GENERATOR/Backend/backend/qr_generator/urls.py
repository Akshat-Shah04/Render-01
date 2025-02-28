# qr_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("generate/", views.generate_qr, name="generate_qr"),
    path("share/<uuid:unique_id>/", views.share_qr, name="share_qr"), # Add this line
]