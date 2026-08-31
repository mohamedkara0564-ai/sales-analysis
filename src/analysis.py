from cleaning import load_and_clean_data
from features import create_features


def calculate_kpis(df):
    """Calcule les indicateurs clés de performance."""

    orders_df = (
        df.groupby("InvoiceNo", as_index=False)
        .agg(
            InvoiceTotal=("Revenue", "sum"),
            TotalQuantity=("Quantity", "sum")
        )
    )

    return {
        "Chiffre d'affaires total": df["Revenue"].sum(),
        "Nombre de commandes": orders_df["InvoiceNo"].nunique(),
        "Nombre de clients": df["CustomerID"].nunique(),
        "Nombre de produits": df["StockCode"].nunique(),
        "Quantité totale vendue": df["Quantity"].sum(),
        "Panier moyen": orders_df["InvoiceTotal"].mean()
    }


if __name__ == "__main__":
    df_clean, _ = load_and_clean_data()
    df_analysis = create_features(df_clean)

    kpis = calculate_kpis(df_analysis)

    for name, value in kpis.items():
        if "affaires" in name or "Panier" in name:
            print(f"{name} : {value:,.2f} £")
        else:
            print(f"{name} : {value:,.0f}")