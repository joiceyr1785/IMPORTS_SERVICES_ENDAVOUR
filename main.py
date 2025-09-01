import pyodbc
import pandas as pd


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=USUARIO-MKQRT2U;'
    'DATABASE=IMPORTS_SERVICES_ENDAVOUR;'
    'Trusted_Connection=yes'
)

# query = "SELECT * FROM Hecho_Licencias_Obras;"
query = " select * from Hecho_Licencias_Obras where id_hecho = 1"
df = pd.read_sql(query, conn)

print(df)
