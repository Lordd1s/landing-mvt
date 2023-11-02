from django.urls import path
from landing_other import views


urlpatterns = [
    path("", views.home, name="home"),
    path("prices/", views.prices, name="prices"),
    path("about/", views.about, name="about"),
]
