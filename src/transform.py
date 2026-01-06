# Archivo: transform.py
# Funciones para extraer y mostrar un resumen básico de datos de ventas.

import pandas as pd

# Explicit exports to ensure the expected symbols are available when importing
__all__ = ["clean_sales_data", "data_quality_report"]


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies data cleaning and transformation rules.
    """

    df = df.copy()

    # 🔹 Normalize text fields
    df["Region"] = df["Region"].str.upper()
    df["Product"] = df["Product"].str.title()
    df["StoreLocation"] = df["StoreLocation"].str.title()
    df["CustomerType"] = df["CustomerType"].str.title()
    df["PaymentMethod"] = df["PaymentMethod"].str.title()
    df["Promotion"] = df["Promotion"].replace("", pd.NA)

    # 🔹 Numeric validations
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]
    df = df[(df["Discount"] >= 0) & (df["Discount"] <= 1)]

    # 🔹 Returned flag normalization
    df["Returned"] = df["Returned"].apply(lambda x: 1 if x == 1 else 0)

    # 🔹 Date validation
    df = df[df["OrderDate"] <= df["DeliveryDate"]]

    # 🔹 Recalculate TotalPrice
    df["CalculatedTotalPrice"] = (
        df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
    ).round(2)

    return df
#reporte de calidad de datos
def data_quality_report(df: pd.DataFrame) -> None:  
    """
    Prints data quality indicators.
    """

    print("📊 DATA QUALITY REPORT")
    print("-" * 30)

    print("\n🔍 Missing values:")
    print(df.isnull().sum())

    print("\n🔢 Duplicated records:")
    print(df.duplicated().sum())

    print("\n📅 Date range:")
    print(f"Orders: {df['OrderDate'].min()} → {df['OrderDate'].max()}")
