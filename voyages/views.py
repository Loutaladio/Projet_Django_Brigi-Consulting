from django.http import Http404
from django.shortcuts import render

from .donnees import DESTINATIONS


def accueil(request):
    coups_de_coeur = [destination for destination in DESTINATIONS if destination["coup_de_coeur"]]
    return render(request, "accueil.html", {"coups_de_coeur": coups_de_coeur[:3]})


def destinations(request):
    return render(request, "destinations.html", {"destinations": DESTINATIONS})


def detail_destination(request, identifiant):
    destination = next((item for item in DESTINATIONS if item["id"] == identifiant), None)
    if destination is None:
        raise Http404("Cette destination n'existe pas dans notre catalogue.")
    return render(request, "detail_destination.html", {"destination": destination})


def a_propos(request):
    return render(request, "a_propos.html")


def contact(request):
    message_envoye = request.method == "POST"
    return render(request, "contact.html", {"message_envoye": message_envoye})
