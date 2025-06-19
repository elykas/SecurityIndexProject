import pandas as pd
from config import FILES


def load_data():
    return pd.read_csv(FILES["flightsData"])