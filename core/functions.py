import csv
import os
import sys
import datetime as dt

from core.config_manager import ConfigManager

SCHULPLAN_PATH = os.path.join("data", "schulplan.csv")

def check_prerequisites():
    """Prüft, ob alle notwendigen Dateien vorhanden sind."""
    if not os.path.exists(SCHULPLAN_PATH):
        print(f"FEHLER: Die Datei '{SCHULPLAN_PATH}' wurde nicht gefunden.")
        print("Bitte erstellen Sie die Datei und fügen Sie Ihre Schulzeiten ein.")
        print("Format: Startdatum;Enddatum;Typ")
        sys.exit(1)
    print(f"OK: '{SCHULPLAN_PATH}' gefunden.")


def load_school_plan(file_path, calendar):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            if not row: continue

            start_str, end_str, school_type = row

            start_date = dt.datetime.strptime(start_str, "%d.%m.%Y").date()
            end_date = dt.datetime.strptime(end_str, "%d.%m.%Y").date()

            current = start_date
            while current <= end_date:
                if current in calendar:
                    calendar[current].school_status = school_type
                current += dt.timedelta(days=1)

    print(f"Schulplan aus {file_path} erfolgreich geladen.")