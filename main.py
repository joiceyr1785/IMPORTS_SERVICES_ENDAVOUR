import pyodbc
import pandas as pd


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=USUARIO-MKQRT2U;'
    'DATABASE=IMPORTS_SERVICES_ENDAVOUR;'
    'Trusted_Connection=yes'
)

query = "SELECT * FROM Hecho_Licencias_Obras;"
df = pd.read_sql(query, conn)

print(df)
