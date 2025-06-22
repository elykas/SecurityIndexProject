from core.loader_base import load_data
from .cleaner import clean_flight_columns
from config import FILES

def load_flights_data():
    flights =load_data(FILES['flightsData'],parse_dates=['CHSTOL'])
    flights = clean_flight_columns(flights)
    return flights