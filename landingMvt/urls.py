from django.urls import path
from landingMvt import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bath/", views.bath, name="bath"),
    path("kitchen/", views.kitchen, name="kitchen"),
    path("interior/", views.interior, name="interior"),
    path("contacts/", views.contacts, name="contacts")
]