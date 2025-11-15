'''
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
    usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
2. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`
'''
import pprint

def buildHotelDetails():
    hotelDetails = {
        'name':'Ace Hotel',
        'starsNumber': 4,
        'rooms' : [
            {
                'number': 120,
                'floor' : 1,
                'priceByNight' : 100
            },
             {
                'number': 303,
                'floor' : 3,
                'priceByNight' : 1001
            },
             {
                'number': 510,
                'floor' : 5,
                'priceByNight' : 10000
            }
        ]
    }
    pprint.pprint(hotelDetails)

def dictionaryBasedOnLists():
    keys = ["nombre", "edad", "ciudad", "profesion", "salario"]
    values = ["Ana", 28, "Madrid", "Diseñadora", 3500]
    identity = dict(zip(keys,values))
    pprint.pprint(identity)

def deletePropertiesIntoDic():
    hotelDetails = {
        'name':'Ace Hotel',
        'starsNumber': 4,
        'rooms' : [
            {
                'number': 120,
                'floor' : 1,
                'priceByNight' : 100
            },
             {
                'number': 303,
                'floor' : 3,
                'priceByNight' : 1001
            },
             {
                'number': 510,
                'floor' : 5,
                'priceByNight' : 10000
            }
        ],
        'direction':""
    }
    keysToDelete = ['name','direction']
    for key in keysToDelete:
        hotelDetails.pop(key,None)
    pprint.pprint(hotelDetails)


buildHotelDetails()
dictionaryBasedOnLists()
deletePropertiesIntoDic()