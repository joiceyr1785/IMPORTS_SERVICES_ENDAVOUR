import pyodbc
from sqlalchemy import create_engine
import pandas as pd

lista_obras = []
ANCHO = 50
opcion = 0

def mostrar_menu(ancho):
    print("="*ancho)
    print(" "*10 + "CRUD DE OBRAS")
    print("="*ancho)
    print("""
          [1] REGISTRAR PROYECTO
          [2] MOSTRAR PROYECTOS
          [3] ACTUALIZAR PROYECTO
          [4] ELIMINAR PROYECTO
          [5] SALIR
          """)
    print("="*ancho)


mostrar_menu(ANCHO)


# CONECTAMOS A LA BASE DE DATOS IMPORT_SERVICES_ENDAVOAR

def conectar_bd(servidor, base_datos, query):

    conn = (
       f"mssql+pyodbc://@{servidor}/{base_datos}"
       "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    engine = create_engine(conn)

    df = pd.read_sql(query, engine)
    return df


if __name__ == "__main__":
    query = "SELECT * FROM Hecho_Licencias_Obras"
    df = conectar_bd("SERVER=USUARIO-MKQRT2U", "DATABASE=IMPORTS_SERVICES_ENDAVOUR", query)
    print(df.head())

