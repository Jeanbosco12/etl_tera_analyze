import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def analyze_data(df):

    print("\n===== STATISTIQUES =====")
    print(df[['pm1', 'pm25', 'pollution_index']].describe())

    # -----------------------------
    # 1. Distribution pollution
    # -----------------------------
    plt.figure()
    sns.histplot(df['pm25'], kde=True)
    plt.title("Distribution PM2.5")
    plt.show()

    # -----------------------------
    # 2. Evolution temporelle
    # -----------------------------
    plt.figure()
    df_sorted = df.sort_values('time')
    plt.plot(df_sorted['time'], df_sorted['pm25'])
    plt.xticks(rotation=45)
    plt.title("Evolution PM2.5 dans le temps")
    plt.show()

    # -----------------------------
    # 3. Comparaison capteurs
    # -----------------------------
    plt.figure()
    sns.boxplot(x='id_install', y='pm25', data=df)
    plt.title("PM2.5 par capteur")
    plt.show()

    # -----------------------------
    # 4. Corrélation
    # -----------------------------
    plt.figure()
    sns.heatmap(df[['pm1', 'pm25', 'pollution_index']].corr(), annot=True)
    plt.title("Corrélation")
    plt.show()

    # -----------------------------
    # 5. Pollution par heure
    # -----------------------------
    plt.figure()
    sns.lineplot(x='hour', y='pm25', data=df)
    plt.title("Pollution selon l'heure")
    plt.show()

    # -----------------------------
    # 6. Détection anomalies
    # -----------------------------
    threshold = df['pm25'].mean() + 2 * df['pm25'].std()
    anomalies = df[df['pm25'] > threshold]

    print("\n⚠️ Anomalies détectées :")
    print(anomalies)

def detect_pollution_peaks(df):

    # Trier par temps
    df = df.sort_values('time')

    # -----------------------------
    # 1. Méthode statistique
    # -----------------------------
    mean = df['pm25'].mean()
    std = df['pm25'].std()

    threshold = mean + 2 * std

    df['peak_stat'] = df['pm25'] > threshold

    print(f"Seuil statistique: {threshold:.2f}")

    # -----------------------------
    # 2. Méthode rolling (fenêtre)
    # -----------------------------
    df['rolling_mean'] = df['pm25'].rolling(window=50).mean()
    df['rolling_std'] = df['pm25'].rolling(window=50).std()

    df['peak_rolling'] = df['pm25'] > (df['rolling_mean'] + 2 * df['rolling_std'])

    # -----------------------------
    # 3. Combinaison intelligente
    # -----------------------------
    df['peak'] = df['peak_stat'] | df['peak_rolling']

    peaks = df[df['peak'] == True]

    print("\n⚠️ Nombre de pics détectés :", len(peaks))

    return df, peaks

def plot_peaks(df):

    plt.figure()

    plt.plot(df['time'], df['pm25'], label='PM2.5')

    # Pics en rouge
    peaks = df[df['peak'] == True]
    plt.scatter(peaks['time'], peaks['pm25'], color='red', label='Pics')

    plt.xticks(rotation=45)
    plt.title("Détection des pics de pollution")
    plt.legend()

    plt.show()