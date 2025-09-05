import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    print("conexion exitosa")
    data = response.json()
    usuario = data['results'][0]
   # print(usuario)
    dic_usuario = {
        'nombre': usuario['name']['first'] + ' ' + usuario['name']['last']
    }
    print(f"Nombre: {dic_usuario['nombre']}")