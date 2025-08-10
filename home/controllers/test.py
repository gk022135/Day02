import json
from django.http import JsonResponse, HttpResponse


def test(request):
    return JsonResponse({
        "success": True,
        "message": "Hi there! It's working fine. Any doubt?"
    })