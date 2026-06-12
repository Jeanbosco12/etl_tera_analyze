import pandas as pd

def extract_csv(path):
    df = pd.read_csv(
        path,
        sep=',',
        skiprows=1,        # 🔥 IGNORE "sep=,"
        low_memory=False
    )

    print("Colonnes détectées :", df.columns)
    print("Shape :", df.shape)

    return df