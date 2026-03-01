'''
5. Cree un programa que le pida al usuario 10 números, y 
    al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

'''

def getHighestNumber():
    userNumbers = []
    for index in range(10):
        number = int(input(f'Digite digito numero {index+1} : '))
        userNumbers.append(number)
    print(f'El digito mas alto es el {max(userNumbers)}')
    
getHighestNumber()
