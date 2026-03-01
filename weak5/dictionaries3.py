'''
3. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`
'''
import pprint


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

deletePropertiesIntoDic()