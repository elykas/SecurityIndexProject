def clean_train_columns(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('"', '')
    )

    column_rename_map = {
        "shana": "year",
        "hodesh": "month",
        "train_trip_cd": "trip_id",
        "first_train_station_nm": "origin_station",
        "last_train_station_nm": "destination_station",
        "rishui_all": "total_registered",
        "rishui_only": "registered_only",
        "bitzua_only": "executed_only",
        "ahuz_bitzua": "execution_rate"
    }

    df.rename(columns=column_rename_map, inplace=True)
    return df