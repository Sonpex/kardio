from django.urls import path
from .views import (
    HomeView,
    LekarzListView,
    PacjentListView,
    UrzadzenieListView,
    PomiarListView,
    LekarzCreateView,
    PacjentCreateView,
    UrzadzenieCreateView,
    PomiarCreateView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("lekarze/", LekarzListView.as_view(), name="lekarz_list"),
    path("pacjenci/", PacjentListView.as_view(), name="pacjent_list"),
    path("urzadzenia/", UrzadzenieListView.as_view(), name="urzadzenie_list"),
    path("pomiary/", PomiarListView.as_view(), name="pomiar_list"),
    path("lekarze/dodaj/", LekarzCreateView.as_view(), name="lekarz_create"),
    path("pacjenci/dodaj/", PacjentCreateView.as_view(), name="pacjent_create"),
    path("urzadzenia/dodaj/", UrzadzenieCreateView.as_view(), name="urzadzenie_create"),
    path("pomiary/dodaj/", PomiarCreateView.as_view(), name="pomiar_create"),
]
