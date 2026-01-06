print("🔥 CARGANDO load.py DESDE:", __file__)

from sqlalchemy import create_engine, text
import pandas as pd

from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

def get_mysql_engine(user, password, host, port, database):
    password_encoded = quote_plus(password)

    connection_string = (
        f"mysql+mysqlconnector://{user}:{password_encoded}@{host}:{port}/{database}"
    )

    print("CONNECTION STRING (SAFE):", connection_string)

    engine = create_engine(connection_string)
    return engine



def create_sales_table(engine):
    """
    Creates sales table with proper schema.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS sales (
        OrderID VARCHAR(20) PRIMARY KEY,
        Region VARCHAR(50),
        RegionManager VARCHAR(50),
        Product VARCHAR(50),
        Quantity INT,
        UnitPrice DECIMAL(10,2),
        Discount DECIMAL(5,2),
        CalculatedTotalPrice DECIMAL(12,2),
        StoreLocation VARCHAR(50),
        CustomerType VARCHAR(30),
        CustomerName VARCHAR(100),
        Salesperson VARCHAR(50),
        PaymentMethod VARCHAR(30),
        Promotion VARCHAR(50),
        Returned TINYINT,
        ShippingCost DECIMAL(10,2),
        OrderDate DATE,
        DeliveryDate DATE
    );
    """

    with engine.connect() as conn:
        conn.execute(text(create_table_sql))


def load_sales_data(engine, df: pd.DataFrame):
    """
    Loads transformed data into MySQL.
    """
    df_to_load = df[
        [
            "OrderID",
            "Region",
            "RegionManager",
            "Product",
            "Quantity",
            "UnitPrice",
            "Discount",
            "CalculatedTotalPrice",
            "StoreLocation",
            "CustomerType",
            "CustomerName",
            "Salesperson",
            "PaymentMethod",
            "Promotion",
            "Returned",
            "ShippingCost",
            "OrderDate",
            "DeliveryDate",
        ]
    ]

    df_to_load.to_sql(
        name="sales",
        con=engine,
        if_exists="append",
        index=False
    )
