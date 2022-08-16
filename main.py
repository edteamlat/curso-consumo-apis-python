import requests
import json

def get_developers():
    response = requests.get('https://apivelopers.com/api/developers')
    result = response.json()['result']
    print(json.dumps(result, indent=4))

def get_developer(id):
    response = requests.get(f'https://apivelopers.com/api/developers/{id}')
    result = response.json()['result']
    print(json.dumps(result, indent=4))

def create_developer():
    data = {
        "name": "Pablo",
        "country": "Ecuador",
        "age": 26,
        "skills": [],
        "experience": [],
        "languages": []
    }
    response = requests.post('https://apivelopers.com/api/developers', json=data)
    result = response.json()['message']
    print(json.dumps(result, indent=4))

def update_developer(id):
    data = {
        "name": "Pablo",
        "country": "Ecuador",
        "age": 26,
        "skills": [
            {
                "name": "Javascript",
                "years": 5
            }
        ],
        "experience": [],
        "languages": []
    }
    response = requests.put(f'https://apivelopers.com/api/developers/{id}', json=data)
    result = response.json()['message']
    print(json.dumps(result, indent=4))


def delete_developer(id):
    response = requests.delete(f'https://apivelopers.com/api/developers/{id}')
    result = response.json()['message']
    print(json.dumps(result, indent=4))

def login():
    data = {
        "username": "user_test",
        "password": "123456"
    }
    response = requests.post(f'https://apivelopers.com/api/auth/login', json=data)
    result = response.json()
    print(json.dumps(result, indent=4))

def init():
    opcion = int(input('Escoja la opción: '))
    print('1. Ver todos los desarrolladores')
    print('2. Ver datos de desarrollador')
    print('3. Registrar desarrollador')
    print('4. Modificar un desarrollador')
    print('5. Eliminar desarrollador')
    print('6. Iniciar sesión')
    if opcion == 1:
        get_developers()
    if opcion == 2:
        id = input('Ingrese el id: ')
        get_developer(id)
    if opcion == 3:
        create_developer()
    if opcion == 4:
        id = input('Ingrese el id: ')
        update_developer(id)
    if opcion == 5:
        id = input('Ingrese el id: ')
        delete_developer(id)
    if opcion == 6:
        login()

if __name__=="__main__":
    init()