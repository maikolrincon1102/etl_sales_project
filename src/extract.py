
# Importamos pandas para manipulación de datos y os para operaciones con archivos
import pandas as pd
import os



# Función para extraer datos de ventas desde un archivo CSV
def extract_sales_data(file_path: str) -> pd.DataFrame:
    """
    Extrae datos de ventas de un archivo CSV y retorna un DataFrame de pandas.

    Args:
        file_path (str): Ruta al archivo CSV

    Returns:
        pd.DataFrame: Datos de ventas extraídos
    """

    # Verificamos si el archivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Leemos el archivo CSV, parseando las fechas relevantes
        df = pd.read_csv(
            file_path,
            sep=",",
            encoding="utf-8",
            parse_dates=["OrderDate", "DeliveryDate"]
        )
    except Exception as e:
        # Si ocurre un error al leer el archivo, lo informamos
        raise Exception(f"Error reading CSV file: {e}")

    # Retornamos el DataFrame resultante
    return df



# Función para mostrar un resumen básico de los datos extraídos
def extract_summary(df: pd.DataFrame) -> None:
    """
    Imprime un resumen básico de los datos extraídos.
    """

    # Mensaje de éxito
    print("✅ Data extracted successfully")
    # Número de filas
    print(f"📦 Rows: {df.shape[0]}")
    # Número de columnas
    print(f"📊 Columns: {df.shape[1]}")
    # Nombres de las columnas
    print("\n🧾 Column names:")
    print(df.columns.tolist())
    # Primeros 5 registros
    print("\n🔍 First 5 records:")
    print(df.head())
