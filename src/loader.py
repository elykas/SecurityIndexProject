import pandas as pd
from config import FILES


def load_data(filename: str, sep: str = ','):
    return pd.read_csv(FILES[filename], sep=sep)