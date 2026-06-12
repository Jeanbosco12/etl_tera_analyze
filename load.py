def load_data(df, path):
    df.to_csv(path, index=False)
    print("Données sauvegardées")