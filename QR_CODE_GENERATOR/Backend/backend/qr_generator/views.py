from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import qrcode
from io import BytesIO
import base64


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

    return Response({"image": img_base64})
