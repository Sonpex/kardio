from django.db import models


class Lekarz(models.Model):
    lekarz_id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=100)
    specjalizacja = models.CharField(max_length=100)

    class Meta:
        ordering = ["nazwisko", "imie"]

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.specjalizacja})"


class Pacjent(models.Model):
    PLEC_CHOICES = [
        ("K", "Kobieta"),
        ("M", "Mężczyzna"),
    ]

    pacjent_id = models.AutoField(primary_key=True)
    lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE, related_name="pacjenci")
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=100)
    data_urodzenia = models.DateField()
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    pesel = models.CharField(max_length=11, unique=True)

    class Meta:
        ordering = ["nazwisko", "imie"]

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Urzadzenie(models.Model):
    urzadzenie_id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    typ_urzadzenia = models.CharField(max_length=50)
    producent = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    numer_seryjny = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nazwa", "model"]

    def __str__(self):
        return f"{self.nazwa} - {self.model}"


class Pomiar(models.Model):
    pomiar_id = models.AutoField(primary_key=True)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE, related_name="pomiary")
    urzadzenie = models.ForeignKey(Urzadzenie, on_delete=models.CASCADE, related_name="pomiary")
    typ_pomiaru = models.CharField(max_length=50)
    pomiar_start = models.DateTimeField()
    pomiar_koniec = models.DateTimeField()
    srednie_tetno = models.PositiveIntegerField()
    min_tetno = models.PositiveIntegerField()
    max_tetno = models.PositiveIntegerField()
    rmssd = models.DecimalField(max_digits=6, decimal_places=2)
    sdnn = models.DecimalField(max_digits=6, decimal_places=2)
    sbp = models.PositiveIntegerField(verbose_name="Średnie ciśnienie skurczowe")
    dbp = models.PositiveIntegerField(verbose_name="Średnie ciśnienie rozkurczowe")

    class Meta:
        ordering = ["-pomiar_start"]

    def __str__(self):
        return f"Pomiar #{self.pomiar_id} - {self.pacjent}"
