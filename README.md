# System monitorowania kardiologicznego

Minimalny projekt Django przygotowany dla tabel:
- Lekarz
- Pacjent
- Urządzenie
- Pomiar

Projekt zawiera:
- modele zgodne ze schematem relacyjnym,
- formularze do dodawania rekordów,
- widoki list danych zapisanych w bazie,
- podstawowe szablony HTML.

## Uruchomienie

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# albo .venv\Scripts\activate na Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Po uruchomieniu wejdź na:
- `/` - strona główna,
- `/lekarze/`, `/pacjenci/`, `/urzadzenia/`, `/pomiary/` - listy rekordów,
- `/lekarze/dodaj/`, `/pacjenci/dodaj/`, `/urzadzenia/dodaj/`, `/pomiary/dodaj/` - formularze.

