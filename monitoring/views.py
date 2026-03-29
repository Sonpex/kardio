from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .forms import LekarzForm, PacjentForm, UrzadzenieForm, PomiarForm
from .models import Lekarz, Pacjent, Urzadzenie, Pomiar


class HomeView(TemplateView):
    template_name = "monitoring/home.html"


class LekarzListView(ListView):
    model = Lekarz
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista lekarzy"
        context["kolumny"] = ["ID", "Imię", "Nazwisko", "Specjalizacja"]
        context["wiersze"] = [[obj.lekarz_id, obj.imie, obj.nazwisko, obj.specjalizacja] for obj in context["obiekty"]]
        context["create_url"] = "/lekarze/dodaj/"
        return context


class PacjentListView(ListView):
    model = Pacjent
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista pacjentów"
        context["kolumny"] = ["ID", "Lekarz", "Imię", "Nazwisko", "Data urodzenia", "Płeć", "PESEL"]
        context["wiersze"] = [[obj.pacjent_id, str(obj.lekarz), obj.imie, obj.nazwisko, obj.data_urodzenia, obj.get_plec_display(), obj.pesel] for obj in context["obiekty"]]
        context["create_url"] = "/pacjenci/dodaj/"
        return context


class UrzadzenieListView(ListView):
    model = Urzadzenie
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista urządzeń"
        context["kolumny"] = ["ID", "Nazwa", "Typ", "Producent", "Model", "Numer seryjny"]
        context["wiersze"] = [[obj.urzadzenie_id, obj.nazwa, obj.typ_urzadzenia, obj.producent, obj.model, obj.numer_seryjny] for obj in context["obiekty"]]
        context["create_url"] = "/urzadzenia/dodaj/"
        return context


class PomiarListView(ListView):
    model = Pomiar
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista pomiarów"
        context["kolumny"] = [
            "ID",
            "Pacjent",
            "Urządzenie",
            "Typ",
            "Start",
            "Koniec",
            "Śr. tętno",
            "Min",
            "Max",
            "RMSSD",
            "SDNN",
            "SBP",
            "DBP",
        ]
        context["wiersze"] = [[obj.pomiar_id, str(obj.pacjent), str(obj.urzadzenie), obj.typ_pomiaru, obj.pomiar_start, obj.pomiar_koniec, obj.srednie_tetno, obj.min_tetno, obj.max_tetno, obj.rmssd, obj.sdnn, obj.sbp, obj.dbp] for obj in context["obiekty"]]
        context["create_url"] = "/pomiary/dodaj/"
        return context


class LekarzCreateView(CreateView):
    model = Lekarz
    form_class = LekarzForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("lekarz_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj lekarza"
        return context


class PacjentCreateView(CreateView):
    model = Pacjent
    form_class = PacjentForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("pacjent_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj pacjenta"
        return context


class UrzadzenieCreateView(CreateView):
    model = Urzadzenie
    form_class = UrzadzenieForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("urzadzenie_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj urządzenie"
        return context


class PomiarCreateView(CreateView):
    model = Pomiar
    form_class = PomiarForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("pomiar_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj pomiar"
        return context
