def create_features(df):
    """Crée les variables nécessaires à l'analyse."""

    df = df.copy()

    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()
    df["Hour"] = df["InvoiceDate"].dt.hour

    df["InvoiceTotal"] = (
        df.groupby("InvoiceNo")["Revenue"].transform("sum")
    )

    return df