'''
3. Cree un programa que intercambie el primer y ultimo elemento de una lista. 
    Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
'''

def switchListPositions():
    listOfNumber = [12, 7, 23, 4, 18, 9, 31, 6, 14, 2]
    listOfNumber[0],listOfNumber[-1] = listOfNumber[-1],listOfNumber[0]
    print(listOfNumber)



switchListPositions()