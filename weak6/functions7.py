'''
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''
def isPrime(number):
    if number < 2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
     

def onlyPrimeNumbers(list):
    primeNumbers= []
    for number in list:
        if isPrime(number):
            primeNumbers.append(number)
    return primeNumbers

print(onlyPrimeNumbers([12, 37, 45, 22, 7, 91, 58, 3, 19, 66, 81, 29, 5, 88, 13]))

