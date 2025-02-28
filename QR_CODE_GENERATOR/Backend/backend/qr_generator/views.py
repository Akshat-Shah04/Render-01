import uuid
from django.http import JsonResponse, HttpResponse
from .models import QRCodeData
from rest_framework.decorators import api_view
from rest_framework.response import Response
import qrcode
from io import BytesIO
import base64
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)


@api_view(["POST"])
def generate_qr(request):
    data = request.data.get("data")
    if not data:
        return Response({"error": "Data is required"}, status=400)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    unique_id = str(uuid.uuid4())
    QRCodeData.objects.create(unique_id=unique_id, image_data=img_base64)

    share_url = f"https://qr-code-xwa2.onrender.com/share/{unique_id}"
    return JsonResponse({"image": img_base64, "share_url": share_url})


def share_qr(request, unique_id):
    logger.info(f"share_qr called with unique_id: {unique_id}")
    qr_data = get_object_or_404(QRCodeData, unique_id=unique_id)
    logger.info(f"QRCodeData found: {qr_data}")
    img_data = base64.b64decode(qr_data.image_data)
    logger.info("Image data decoded")
    return HttpResponse(img_data, content_type="image/png")
