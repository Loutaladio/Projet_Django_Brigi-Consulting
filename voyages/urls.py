from django.urls import path
from . import views

app_name = "voyages"

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("destinations/", views.destinations, name="destinations"),
    path("destinations/<str:identifiant>/", views.detail_destination, name="detail_destination"),
    path("a-propos/", views.a_propos, name="a_propos"),
    path("contact/", views.contact, name="contact"),
]
