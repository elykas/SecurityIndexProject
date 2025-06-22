import pandas as pd

def calculate_monthly_trains_execution(trains: pd.DataFrame) -> pd.DataFrame:
    trains = trains.copy()
    trains['date'] = pd.to_datetime(trains['year'].astype(str) + '-' + trains['month'].astype(str), format='%Y-%m')
    monthly_execution_rate = trains.groupby('date')['execution_rate'].mean().reset_index()
    return monthly_execution_rate.set_index('date')
