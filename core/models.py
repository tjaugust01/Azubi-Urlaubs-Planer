import csv
import datetime as dt

import holidays


class Day:
    def __init__(self, date: dt.date):
        self.day = date
        self.is_weekend = date.weekday() >= 5
        self.holiday_name = None
        self.school_status = "WORK"
        self.is_fixed_vacation = False

    @property
    def real_type(self) -> str:
        if self.holiday_name:
            return "HOLIDAY"
        if self.is_weekend:
            return "WEEKEND"
        if self.is_fixed_vacation:
            return "FIXEDVACATION"
        # HIER: Prüfe auf die exakten Begriffe aus deiner CSV
        if self.school_status == "SCHULE_GESCHLOSSEN":
            return "SCHOOL_CLOSED"
        if self.school_status == "SCHULE":
            return "SCHOOL"
        return "WORK"

    def is_plannable(self) -> bool:
        return self.real_type in ["WORK", "SCHOOL_CLOSED"]


    def __repr__(self):
        return f"Day(Type={self.real_type})"

class CalendarBuilder:
    def __init__(self, year: int, state: str = "SN"):
        self.year = year
        self.state = state
        self.calendar = {}
        self.create_empty_calender()
        print("ADEADASD")
        print(self.year)

    def create_empty_calender(self):
        start_date = dt.date(self.year, 1, 1)
        end_date = dt.date(self.year, 12, 31)

        while start_date <= end_date:
            self.calendar[start_date] = Day(start_date)

            start_date += dt.timedelta(days=1)

    def load_holidays(self):
        de_holidays = holidays.Germany(prov=self.state, years=self.year)
        for date, name in de_holidays.items():
            if date in self.calendar:
                self.calendar[date].holiday_name = name

    def apply_school_plan(self, file_path):
        print(f"Versuche Datei zu laden: {file_path}")
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                print(f"DEBUG: Gefundene Zeile -> {row}")
                start_date = dt.datetime.strptime(row[0], "%d.%m.%Y").date()
                end_date = dt.datetime.strptime(row[1], "%d.%m.%Y").date()
                s_type = row[2]

                curr = start_date
                while curr <= end_date:
                    if curr in self.calendar:
                        self.calendar[curr].school_status = s_type
                    curr += dt.timedelta(days=1)