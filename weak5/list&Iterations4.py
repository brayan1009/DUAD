'''
4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`
'''


def notOddNumbers():
    listOfNumber = [12, 7, 23, 4, 18, 9, 31, 6, 14, 2]
    evenNumbers = []
    for number in listOfNumber:
        if number % 2 == 0:
            evenNumbers.append(number)
    print(evenNumbers)


notOddNumbers()
