import pandas as pd
def clean_dates(df:pd.DataFrame, date_column:str, year_column:str = 'year') -> pd.DataFrame:
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column],errors='coerce')
    df[date_column] = df[date_column].dt.year
    return df