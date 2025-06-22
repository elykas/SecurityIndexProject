def calculate_daily_cancel_rate(flights):
    flights = flights.copy()

    flights['date'] = flights['scheduled_takeoff'].dt.date

    flights['status_eng'] = flights['status_eng'].str.lower()

    flights['canceled'] = flights['status_eng'] == 'canceled'

    daily_cancel_rate = flights.groupby('date')['canceled'].mean().reset_index()

    daily_cancel_rate.rename(columns={'canceled': 'cancel_rate'}, inplace=True)
    daily_cancel_rate['cancel_rate'] *= 100

    return daily_cancel_rate

