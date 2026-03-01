'''
2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    1. Pista: investigue de que otras maneras se puede usar el `range`.
    2. Ejemplos:
    3. `my_string = 'Pizza con piña’` → 
    a
    ñ
    i
    p
    
    n
    o
    c
    
    a
    z
    z
    i
    p
'''

def printTextLetterByLetter():
    textToPrint = 'Esto es una prueba'
    for index in range(0,len(textToPrint)):
        print(textToPrint[index])




printTextLetterByLetter()