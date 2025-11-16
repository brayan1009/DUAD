'''
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
'''

def reverseString(value):
    return ''.join(reversed(value))

print(f'Texto en reversa es {reverseString("Hola Mundo")}')

