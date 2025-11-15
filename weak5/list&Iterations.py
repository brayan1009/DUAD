'''
💪🏽 **Ejercicios**

**Para estos ejercicios debe utilizar solo lo visto en clase. No es valido utilizar funciones como `zip` o `reversed`.**

1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, 'en’, 'que’, 'iteracion’, 'indices’, 'muy’]`
    `second_list = [’casos’, 'los’, 'la’, 'por’, 'es’, 'util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util
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
3. Cree un programa que intercambie el primer y ultimo elemento de una lista. 
    Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`
5. Cree un programa que le pida al usuario 10 números, y 
    al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

'''

def twoListAtTime():
    first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
    second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

    for index in range(0,len(first_list)):
        print(f'{first_list[index]} {second_list[index]}', end=" ")
    print("")

def printTextLetterByLetter():
    textToPrint = 'Esto es una prueba'
    for index in range(0,len(textToPrint)):
        print(textToPrint[index])

def switchListPositions():
    listOfNumber = [12, 7, 23, 4, 18, 9, 31, 6, 14, 2]
    listOfNumber[0],listOfNumber[-1] = listOfNumber[-1],listOfNumber[0]
    print(listOfNumber)

def notOddNumbers():
    listOfNumber = [12, 7, 23, 4, 18, 9, 31, 6, 14, 2]
    evenNumbers = []
    for number in listOfNumber:
        if number % 2 == 0:
            evenNumbers.append(number)
    print(evenNumbers)

def getHighestNumber():
    userNumbers = []
    for index in range(10):
        number = int(input(f'Digite digito numero {index+1} : '))
        userNumbers.append(number)
    print(f'El digito mas alto es el {max(userNumbers)}')

twoListAtTime()
printTextLetterByLetter()
switchListPositions()
notOddNumbers()
getHighestNumber()
