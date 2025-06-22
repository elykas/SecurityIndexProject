import pandas as pd

def load_data(filepath: str, sep: str = ',', **kwargs):
    return pd.read_csv(filepath, sep=sep, **kwargs)