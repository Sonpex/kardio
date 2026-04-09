from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .forms import LekarzForm, PacjentForm, UrzadzenieForm, PomiarForm
from .models import Lekarz, Pacjent, Urzadzenie, Pomiar


class HomeView(TemplateView):
    template_name = "monitoring/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["liczba_lekarzy"] = Lekarz.objects.count()
        context["liczba_pacjentow"] = Pacjent.objects.count()
        context["liczba_urzadzen"] = Urzadzenie.objects.count()
        context["liczba_pomiarow"] = Pomiar.objects.count()
        context["ostatnie_pomiary"] = Pomiar.objects.select_related("pacjent", "urzadzenie")[:5]
        return context


class LekarzListView(ListView):
    model = Lekarz
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista lekarzy"
        context["opis"] = "Widok wszystkich lekarzy dostępnych w systemie."
        context["kolumny"] = ["ID", "Imię", "Nazwisko", "Specjalizacja"]
        context["wiersze"] = [[obj.lekarz_id, obj.imie, obj.nazwisko, obj.specjalizacja] for obj in context["obiekty"]]
        context["create_url"] = "/lekarze/dodaj/"
        context["ikonka"] = "person-badge"
        return context


class PacjentListView(ListView):
    model = Pacjent
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista pacjentów"
        context["opis"] = "Pacjenci przypisani do lekarzy prowadzących."
        context["kolumny"] = ["ID", "Lekarz", "Imię", "Nazwisko", "Data urodzenia", "Płeć", "PESEL"]
        context["wiersze"] = [[obj.pacjent_id, str(obj.lekarz), obj.imie, obj.nazwisko, obj.data_urodzenia, obj.get_plec_display(), obj.pesel] for obj in context["obiekty"]]
        context["create_url"] = "/pacjenci/dodaj/"
        context["ikonka"] = "people-fill"
        return context


class UrzadzenieListView(ListView):
    model = Urzadzenie
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista urządzeń"
        context["opis"] = "Urządzenia wykorzystywane do tworzenia zagregowanych pomiarów."
        context["kolumny"] = ["ID", "Nazwa", "Typ", "Producent", "Model", "Numer seryjny"]
        context["wiersze"] = [[obj.urzadzenie_id, obj.nazwa, obj.typ_urzadzenia, obj.producent, obj.model, obj.numer_seryjny] for obj in context["obiekty"]]
        context["create_url"] = "/urzadzenia/dodaj/"
        context["ikonka"] = "cpu-fill"
        return context


class PomiarListView(ListView):
    model = Pomiar
    template_name = "monitoring/list.html"
    context_object_name = "obiekty"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Lista pomiarów"
        context["opis"] = "Każdy rekord reprezentuje jedno okno czasowe z wyliczonymi agregatami parametrów."
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
        context["ikonka"] = "activity"
        return context


class LekarzCreateView(CreateView):
    model = Lekarz
    form_class = LekarzForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("lekarz_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj lekarza"
        context["opis"] = "Formularz tworzenia nowego lekarza w bazie."
        context["ikonka"] = "person-badge"
        return context


class PacjentCreateView(CreateView):
    model = Pacjent
    form_class = PacjentForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("pacjent_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj pacjenta"
        context["opis"] = "Nowy pacjent zostanie przypisany do wybranego lekarza."
        context["ikonka"] = "people-fill"
        return context


class UrzadzenieCreateView(CreateView):
    model = Urzadzenie
    form_class = UrzadzenieForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("urzadzenie_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj urządzenie"
        context["opis"] = "Dodawanie urządzeń pomiarowych dostępnych w systemie."
        context["ikonka"] = "cpu-fill"
        return context


class PomiarCreateView(CreateView):
    model = Pomiar
    form_class = PomiarForm
    template_name = "monitoring/form.html"
    success_url = reverse_lazy("pomiar_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tytul"] = "Dodaj pomiar"
        context["opis"] = "Zapis zagregowanego okna czasowego z parametrami HRV i ciśnieniem."
        context["ikonka"] = "clipboard-pulse"
        return context
