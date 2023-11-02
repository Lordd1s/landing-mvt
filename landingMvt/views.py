from django.shortcuts import render, redirect
from django.urls import reverse

from landingMvt import models


# Create your views here.
def index(request):
    return render(request, "landing_first/index.html")


def bath(request):
    return render(request, "landing_first/bath.html")


def kitchen(request):
    return render(request, "landing_first/kitchen.html")


def interior(request):
    return render(request, "landing_first/interior.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        email = request.POST.get("email", "")
        phone_number = request.POST.get("phonenum", "")
        address = request.POST.get("address", "")
        theme = request.POST.get("theme", "")

        if not name or (not email and not phone_number) or not theme:
            return render(request, "index.html", {"error": "Заполните нужные поля!"})

        models.Contact.objects.create(
            first_name=name,
            surname=surname,
            email=email,
            phone=phone_number,
            address=address,
            theme=theme,
        )
        return render(
            request,
            "landing_first/index.html",
            {"success": "Ваша заявка принята! Ожидайте ответа в течении 15 минут!"},
        )
    else:
        return render(
            request, "landing_first/index.html", {"error": "Ошибка при отправке формы!"}
        )
