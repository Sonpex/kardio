from django import forms
from .models import Lekarz, Pacjent, Urzadzenie, Pomiar


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class LekarzForm(forms.ModelForm):
    class Meta:
        model = Lekarz
        fields = ["imie", "nazwisko", "specjalizacja"]


class PacjentForm(forms.ModelForm):
    class Meta:
        model = Pacjent
        fields = ["lekarz", "imie", "nazwisko", "data_urodzenia", "plec", "pesel"]
        widgets = {
            "data_urodzenia": forms.DateInput(attrs={"type": "date"}),
        }


class UrzadzenieForm(forms.ModelForm):
    class Meta:
        model = Urzadzenie
        fields = ["nazwa", "typ_urzadzenia", "producent", "model", "numer_seryjny"]


class PomiarForm(forms.ModelForm):
    class Meta:
        model = Pomiar
        fields = [
            "pacjent",
            "urzadzenie",
            "typ_pomiaru",
            "pomiar_start",
            "pomiar_koniec",
            "srednie_tetno",
            "min_tetno",
            "max_tetno",
            "rmssd",
            "sdnn",
            "sbp",
            "dbp",
        ]
        widgets = {
            "pomiar_start": DateTimeLocalInput(),
            "pomiar_koniec": DateTimeLocalInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("pomiar_start")
        koniec = cleaned_data.get("pomiar_koniec")
        min_tetno = cleaned_data.get("min_tetno")
        srednie = cleaned_data.get("srednie_tetno")
        max_tetno = cleaned_data.get("max_tetno")

        if start and koniec and koniec <= start:
            self.add_error("pomiar_koniec", "Koniec pomiaru musi być późniejszy niż początek.")

        if None not in (min_tetno, srednie, max_tetno) and not (min_tetno <= srednie <= max_tetno):
            self.add_error("srednie_tetno", "Średnie tętno powinno mieścić się pomiędzy min i max.")

        return cleaned_data
