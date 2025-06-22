def clean_flight_columns(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('"', '')
    )

    column_rename_map = {
        "choper": "airline_code",
        "chfltn": "flight_number",
        "choperd": "airline_name",
        "chstol": "scheduled_takeoff",
        "chptol": "actual_takeoff",
        "chaord": "terminal_direction",
        "chloc1": "destination_airport_code",
        "chloc1d": "destination_airport_name_eng",
        "chloc1th": "destination_city_name_heb",
        "chloc1t": "destination_city_name_eng",
        "chloc1ch": "destination_country_name_heb",
        "chlocct": "destination_country_name_eng",
        "chterm": "terminal",
        "chcint": "international_indicator",
        "chckzn": "security_zone",
        "chrmine": "status_eng",
        "chrminh": "status_heb"
    }

    df.rename(columns=column_rename_map, inplace=True)

    return df
