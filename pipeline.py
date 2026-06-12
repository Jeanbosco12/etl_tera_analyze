from drarisetra.extract import extract_csv
from drarisetra.transform import transform_data
from drarisetra.analyze import analyze_data, detect_pollution_peaks, plot_peaks
from drarisetra.load import load_data
def run_pipeline():

    df = extract_csv("tera_analytics_data.csv")
    df = transform_data(df)
    analyze_data(df)
    df, peaks = detect_pollution_peaks(df)
    plot_peaks(df)
    load_data(df, "cleaned_data.csv")

if __name__ == "__main__":
    run_pipeline()