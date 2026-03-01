'''
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`

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



buildHotelDetails()