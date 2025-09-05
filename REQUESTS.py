import requests
import pyodbc

def random_users(count = 100):
    url = f'https://randomuser.me/api/?results={count}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print('error : ', response.status_code)
        return []

def insert_users_sql_server(users):
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server}; "
        "SERVER=USUARIO-MKQRT2U;"
        "DATABASE=api;"
        "Trusted_Connection=yes;"
    )

    cursor = connection.cursor()

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name= 'tbl_usuario' AND xtype='U')
        CREATE TABLE tbl_usuario (
            id INT IDENTITY(1,1) PRIMARY KEY,
            nombre NVARCHAR(255),
            email NVARCHAR(255),
            pais NVARCHAR(255),
            foto NVARCHAR(255)
        )
    """)
    connection.commit()

    for usuario in users:
        nombre = usuario['name']['first'] + ' ' + usuario['name']['last']
        pais = usuario['location']['country']
        email = usuario['email']
        foto = usuario['picture']['large']

        cursor.execute("""
           INSERT INTO tbl_usuario(nombre, pais, email, foto)
           VALUES (?, ?, ?, ?)
           """, (nombre, pais, email, foto)
        )

    connection.commit()
    cursor.close()
    connection.close()

#main
count_usuarios = int(input("Inserte cantidad de usuarios a extraer: "))
usuarios = random_users(count_usuarios)
print("usarios obtenido: ", len(usuarios))
insert_users_sql_server(usuarios)

