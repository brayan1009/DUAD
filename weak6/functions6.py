'''
6. Cree una función que acepte un string con palabras separadas por un guión 
    y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''


def sortString(text):
    listOfWords = sorted(text.split('-'))
    return '-'.join(listOfWords)

print(sortString('python-variable-funcion-computadora-monitor'))

