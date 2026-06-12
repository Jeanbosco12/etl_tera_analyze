import pandas as pd
def transform_data(df):

    # Conversion date
    df['time'] = pd.to_datetime(df['time'])

    # Nettoyage
    df = df.drop_duplicates()
    df = df.dropna()

    # Types numériques
    df['pm1'] = pd.to_numeric(df['pm1'], errors='coerce')
    df['pm25'] = pd.to_numeric(df['pm25'], errors='coerce')

    # Feature engineering
    df['hour'] = df['time'].dt.hour
    df['day'] = df['time'].dt.date

    # Indice pollution simple
    df['pollution_index'] = (df['pm1'] + df['pm25']) / 2

    print("Transformation terminée")
    return df