import datetime as dt
from pprint import pprint

from core.models import CalendarBuilder


def create_calender(year):
    print("Creating calendar object1111")
    builder = CalendarBuilder(year, state="SN")
    print("Creating calendar object")
    builder.load_holidays()
    builder.apply_school_plan("data/schulplan.csv")
    pprint(builder.calendar)
    print("dasd")