import os
import tabulate
import pandas as pd
from sqlalchemy import create_engine, text

ANCHO = 50
opcion = 0

def mostrar_menu(ancho):
    print("="*ancho)
    print(" "*10 + "CRUD DE UBICACIONES")
    print("="*ancho)
    print("""
          [1] REGISTRAR PROYECTO
          [2] MOSTRAR PROYECTOS
          [3] ACTUALIZAR PROYECTO
          [4] ELIMINAR PROYECTO
          [5] SALIR
          """)
    print("="*ancho)


# CONECTAMOS A LA BASE DE DATOS IMPORT_SERVICES_ENDAVOAR
def conectar_bd(servidor, base_datos):
    conn = (
       f"mssql+pyodbc://@{servidor}/{base_datos}"
       "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    engine = create_engine(conn)
    return engine

def muestra_query(engine, query):
    df = pd.read_sql(query, engine)
    return df

def insertar_proyecto(engine, distrito, provincia, departamento, region):
    query = text("""
        INSERT INTO Dim_Ubicacion(distrito, provincia, departamento, region)
        VALUES (:distrito, :provincia, :departamento, :region)
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            "distrito": distrito,
            "provincia": provincia,
            "departamento": departamento,
            "region": region
        })
def busqueda_ubicacion(engine, id_ubicacion):
    query = text("""
         SELECT * 
         FROM Dim_Ubicacion 
         where id_ubicacion = :id_ubicacion
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"id_ubicacion": id_ubicacion})
    return df

def actualizamos_ubicacion(engine, id_ubicacion, nuevo_distrito, nueva_provincia, nuevo_departamento, nueva_region):
    query = text("""
        UPDATE Dim_Ubicacion
        SET distrito = :distrito,
            provincia = :provincia,
            departamento = :departamento,
            region = :region
        WHERE id_ubicacion = :id
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            "distrito": nuevo_distrito,
            "provincia": nueva_provincia,
            "departamento": nuevo_departamento,
            "region": nueva_region,
            "id": id_ubicacion
        })
    print(f"Proyecto con ID {id_ubicacion} actualizado correctamente. ")

def eliminar_ubicacion(engine, id_ubicacion):
    query = text("""
        DELETE FROM Dim_Ubicacion Where id_ubicacion = :id
    """)
    with engine.begin() as conn:
        conn.execute(query, {"id": id_ubicacion})
    print(f"Proyecto con ID {id_ubicacion} elimanado")
"""
if __name__ == "__main__":
    mostrar_menu(ANCHO)
    # CONEXIÓN DE LA BASE DE DATOS
    engine = conectar_bd("USUARIO-MKQRT2U", "IMPORTS_SERVICES_ENDAVOUR")

    # INSERT DATA EN LA BBDD
    insertar_proyecto(engine, "San Juan de Miraflores", "Lima", "Lima", "Costa")

    # MOSTRAR la tabla hechos
    query = "SELECT * FROM Dim_Ubicacion;"
    df = muestra_query(engine, query)
    print(df.head())

    # BUSQUEDA de un elemento en especifico
    df = busqueda_ubicacion(engine, 2204)
    print(df)

    # UPDATE la tabla deseada
    df = actualizamos_ubicacion(engine,
                                id_ubicacion= 2204,
                                nuevo_distrito= "La Victoria",
                                nueva_provincia= "Lima",
                                nuevo_departamento="Lima",
                                nueva_region= "Costa")
    print(df)


    # DELETE un elemento de la tabla Dim_Ubicacion
    eliminar_ubicacion(engine,2215)

"""
if __name__ == "__main__":
    engine = conectar_bd("USUARIO-MKQRT2U", "IMPORTS_SERVICES_ENDAVOUR")

    while opcion != 5:
        os.system("cls")
        mostrar_menu(ANCHO)
        opcion = int(input("Ingrese una opción: "))
        os.system("cls")

        if opcion == 1:
            print("="*ANCHO)
            print(" " * 10 + "[1] INGRESA UBICACION")
            print("="*ANCHO)
            ubicacion = input("ID_UBICACON: ")
            distrito = input("DISTRITO: ")
            provincia = input("PROVINCIA: ")
            departamento = input("DEPARTAMENTO")
            region = input("REGION")
            insertar_proyecto(engine, distrito, provincia, departamento, region)
            print("UBICACION INGRESADA CON EXITO")
            input("Presiona ENTER para continuar... ")

        elif opcion == 2:
            print(" = "*ANCHO)
            print(" "*10 + "[2] MOSTRAR UBICACIONES")
            print("="*ANCHO)
            query = "Select * from Dim_Ubicacion"
            df = muestra_query(engine, query)
            if df.empty:
                print("No hay registros en la tabla Dim_Ubicaion. ")
            else:
                print(tabulate.tabulate(df, headers="Keys", tablefmt="grid"))
            print("Presione ENTER para continuar ...")

        elif opcion == 3:
            print("="*ANCHO)
            print(" "*10 + "[3] ACTUALIZAR UBICACION")
            print("="*ANCHO)
            id_ubicacion = int(input("Ingrese ID_UBICACION a actualizar: "))
            df = busqueda_ubicacion(engine, id_ubicacion)
            if df.empty:
                print("No se encontró la ubicacion con ese id_ubicacion. ")
            else:
                print("Ubicación actual: ", df.to_dict(orient="records"))
                nuevo_distrito = input("Nuevo DISTRITO: ")
                nueva_provincia = input("Nueva PROVINCIA: ")
                nuevo_departamento = input("Nuevo DEPARTAMENTO: ")
                nueva_region = input("Nueva REGIÓN")
                actualizamos_ubicacion(engine, id_ubicacion, nuevo_distrito, nueva_provincia, nuevo_departamento, nueva_region)
            input("Presione ENTER para continuar ...")

        elif opcion == 4:
            print("="*ANCHO)
            print(" "*10 + "[4] ELIMINAR UBICACION")
            print("="*ANCHO)
            id_ubicacion = int(input("Ingrese la ubicacion a eliminar"))
            df = busqueda_ubicacion(engine,id_ubicacion)
            if df.empty:
                print("NO SE ENCONTRO LA UBICACION SOLICITADA")
            else:
                eliminar_ubicacion(engine, id_ubicacion)
            input("Presiona ENTER para continuar")
        elif opcion == 5:
            print("="*ANCHO)
            print(" "*10 + "SALIENDO DEL MENU")
            print("="*ANCHO)

        else:
            print("Opcion invalida. ")
            input("Presione ENTER para continuar")
