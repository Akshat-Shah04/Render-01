from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import SuspiciousOperation
from .models import URL
import uuid


def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get("long_url")

        if original_url:
            # Ensure the URL starts with http:// or https://
            if not original_url.startswith(("http://", "https://")):
                original_url = "http://" + original_url  # Default to http

            # Check if the URL already exists
            url_entry, created = URL.objects.get_or_create(
                original_url=original_url, defaults={"short_id": uuid.uuid4().hex[:6]}
            )

            # Store the shortened URL
            short_url = request.build_absolute_uri(f"/shortener/{url_entry.short_id}")

            # Store it in session temporarily and redirect to avoid form resubmission
            request.session["short_url"] = short_url
            return redirect("/shortener/")

    # Get the short URL from session and then delete it
    short_url = request.session.pop("short_url", None)

    return render(request, "index.html", {"short_url": short_url})


def redirect_url(request, short_id):
    # Fetch the original URL, return 404 if not found
    url_entry = get_object_or_404(URL, short_id=short_id)
    original_url = url_entry.original_url

    # Ensure only http:// or https:// URLs are redirected to
    if not original_url.startswith(("http://", "https://")):
        raise SuspiciousOperation("Unsafe redirect attempted.")

    return redirect(original_url)


def custom_404(request, exception):
    return render(request, "error404.html", status=404)
