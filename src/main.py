from indicators.trains.loader import load_train_data
from indicators.trains.preprocess import calculate_monthly_trains_execution

from indicators.flights.loader import load_flights_data
from indicators.flights.preprocess import calculate_daily_cancel_rate

def main():
    trains = load_train_data()
    monthly_execution = calculate_monthly_trains_execution(trains)
    print(monthly_execution.head())


    flights = load_flights_data()
    flights = calculate_daily_cancel_rate(flights)
    print(flights.head())



if __name__ == "__main__":
    main()
