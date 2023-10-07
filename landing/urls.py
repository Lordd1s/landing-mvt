from django.urls import path
from landing import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bath/", views.bath, name="bath"),
    path("kitchen/", views.kitchen, name="kitchen"),
    path("interior/", views.interior, name="interior"),
    path("contacts/", views.contacts, name="contacts")
]