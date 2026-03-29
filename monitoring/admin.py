from django.contrib import admin
from .models import Lekarz, Pacjent, Urzadzenie, Pomiar

admin.site.register(Lekarz)
admin.site.register(Pacjent)
admin.site.register(Urzadzenie)
admin.site.register(Pomiar)
