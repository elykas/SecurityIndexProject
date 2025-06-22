from loader import load_data
from preprocess import calculate_monthly_trains_execution


def main():
    df_trains = load_data('trainData', sep='|')
    monthly_trains_execution = calculate_monthly_trains_execution(df_trains)

    
