from pathlib import Path

# =========================
# IMPORTS
# =========================
from src.extract import extract_sales_data
from src.transform import clean_sales_data, data_quality_report
from src.load import get_mysql_engine, create_sales_table, load_sales_data

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "raw" / "sales_data.csv"

# =========================
# DATABASE CONFIG
# =========================
USER = "root"
PASSWORD = "T3quierovid@mia"
HOST = "localhost"
PORT = 3306
DATABASE = "sales_dw"

# =========================
# ETL PIPELINE
# =========================
df_raw = extract_sales_data(FILE_PATH)
df_transformed = clean_sales_data(df_raw)

data_quality_report(df_transformed)

print("\n✅ Transformed data preview:")
print(df_transformed.head())

engine = get_mysql_engine(USER, PASSWORD, HOST, PORT, DATABASE)
create_sales_table(engine)
load_sales_data(engine, df_transformed)

print("\n✅ Data loaded successfully into MySQL")
