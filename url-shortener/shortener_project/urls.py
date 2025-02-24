from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shortener/", include("shortener.urls")),
]


from django.conf.urls import handler404
from shortener.views import custom_404  # Import your custom 404 view

handler404 = "shortener.views.custom_404"  # Use the full path to the function
