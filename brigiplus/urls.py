from django.urls import include, path

urlpatterns = [
    path("", include("voyages.urls")),
]
