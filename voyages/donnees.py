"""Catalogue statique de Brigi+ Consulting.

Ce module remplace volontairement une base de données pour l'exercice.
Chaque dictionnaire représente une offre indépendante.
"""

DESTINATIONS = [
    {
        "id": "zanzibar",
        "titre": "Zanzibar, l'île aux épices",
        "pays": "Tanzanie",
        "prix": 846000,
        "duree": "8 jours / 7 nuits",
        "image": "images/real/zanzibar.jpg",
        "accroche": "Lagons turquoise, sable blanc et parfums d'épices.",
        "description": "Une parenthèse insulaire entre les ruelles historiques de Stone Town, les plages de Nungwi et une sortie en mer au coucher du soleil. Zanzibar se découvre lentement, au rythme des dhows et des marchés colorés.",
        "coup_de_coeur": True,
        "inclus": ["Vols aller-retour", "Hôtel 4 étoiles avec petit-déjeuner", "Excursion aux épices", "Transferts aéroport"],
    },
    {
        "id": "kyoto",
        "titre": "Kyoto, l'élégance intemporelle",
        "pays": "Japon",
        "prix": 1438000,
        "duree": "10 jours / 9 nuits",
        "image": "images/real/kyoto.jpg",
        "accroche": "Temples paisibles, jardins zen et traditions vivantes.",
        "description": "De Gion aux forêts de bambous d'Arashiyama, ce voyage révèle un Japon délicat et contrasté. Une immersion entre cérémonie du thé, gastronomie raffinée et escapade à Nara.",
        "coup_de_coeur": True,
        "inclus": ["Vols internationaux", "Hôtels soigneusement sélectionnés", "Pass ferroviaire régional", "Visite guidée de Nara"],
    },
    {
        "id": "patagonie",
        "titre": "Patagonie, souffle austral",
        "pays": "Argentine & Chili",
        "prix": 1824000,
        "duree": "12 jours / 11 nuits",
        "image": "images/real/patagonie.jpg",
        "accroche": "Glaciers, grands espaces et randonnées d'exception.",
        "description": "Une aventure au bout du monde, des passerelles du glacier Perito Moreno aux sentiers du parc Torres del Paine. Un itinéraire pensé pour les amoureux de nature et de panoramas grandioses.",
        "coup_de_coeur": False,
        "inclus": ["Vols et vols intérieurs", "Écolodges et hôtels", "Guide francophone", "Transferts et entrées des parcs"],
    },
    {
        "id": "marrakech",
        "titre": "Marrakech, lumière rouge",
        "pays": "Maroc",
        "prix": 453000,
        "duree": "5 jours / 4 nuits",
        "image": "images/real/marrakech.jpg",
        "accroche": "Une escapade sensorielle entre médina et désert.",
        "description": "Un séjour vibrant au cœur de la ville ocre : riad confidentiel, cuisine généreuse, artisanat et parenthèse dans le désert d'Agafay. Une destination dépaysante à quelques heures de vol.",
        "coup_de_coeur": True,
        "inclus": ["Vols aller-retour", "Riad de charme", "Dîner dans le désert", "Transferts privés"],
    },
    {
        "id": "reunion",
        "titre": "La Réunion, terre intense",
        "pays": "France",
        "prix": 1010000,
        "duree": "9 jours / 8 nuits",
        "image": "images/real/reunion.jpg",
        "accroche": "Volcans, cirques et horizons de l'océan Indien.",
        "description": "Un itinéraire actif entre le piton de la Fournaise, les villages créoles et les panoramas du cirque de Cilaos. La Réunion offre une incroyable diversité sur une seule île.",
        "coup_de_coeur": False,
        "inclus": ["Vols internationaux", "Véhicule de location", "Hébergements de charme", "Carnet de route personnalisé"],
    },
]
