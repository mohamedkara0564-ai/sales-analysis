from pathlib import Path
import pandas as pd


# Chemin vers le dossier principal du projet
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "data.csv"


def load_and_clean_data(csv_path=DATA_PATH):
    """Charge et nettoie les données de ventes e-commerce."""

    # Chargement
    df = pd.read_csv(csv_path, encoding="latin-1")

    # Conversion de la date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Conservation des annulations pour une éventuelle analyse
    df_cancelled = df[
        df["InvoiceNo"].astype(str).str.startswith("C")
    ].copy()

    # Nettoyage
    df_clean = df.copy()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna(subset=["Description", "CustomerID"])

    df_clean = df_clean[
        ~df_clean["InvoiceNo"].astype(str).str.startswith("C")
    ].copy()

    df_clean = df_clean[
        (df_clean["Quantity"] > 0) &
        (df_clean["UnitPrice"] > 0)
    ].copy()

    # Identifiant client sous forme entière
    df_clean["CustomerID"] = df_clean["CustomerID"].astype(int)

    return df_clean, df_cancelled


if __name__ == "__main__":
    df_clean, df_cancelled = load_and_clean_data()

    print("Nombre de lignes nettoyées :", len(df_clean))
    print("Nombre d'annulations :", len(df_cancelled))