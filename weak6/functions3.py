'''
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''

def sumList(list):
    return sum(list)

print(f'La suma de los numeros es {sumList([4, 6, 2, 29])}')
