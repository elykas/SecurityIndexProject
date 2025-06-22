import pandas as pd

def preprocess_flights(dataFrame):
    return dataFrame

def calculate_monthly_trains_execution(dataFrame):
    df = dataFrame.copy()
    
    df['date'] = pd.to_datetime(df['shana'].astype(str) + '-' + df['hodesh'].astype(str), format='%Y-%m')

    grouped = df.groupby('date')['achuz-bitsua'].mean().reset_index()

    return grouped.set_index('date')    