'''
💪🏽 **Ejercicios**

1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
'''
def printOtherThing():
    print('other thing')

def printOneThing():
    print(f"Im just printing", end=" ")
    printOtherThing()

printOneThing()

globalNumber = 1000

def scopingVariables():
    global globalNumber #debe declararse asi para que el valor pueda modificarse, si no, es una variable local mas
    localNumber = 100;
    globalNumber = 10000

scopingVariables()
print(globalNumber)

#globalNumber = localNumber Da error al no reconocerla

def sumList(list):
    return sum(list)

print(f'La suma de los numeros es {sumList([4, 6, 2, 29])}')

def reverseString(value):
    return ''.join(reversed(value))

print(f'Texto en reversa es {reverseString("Hola Mundo")}')
'''
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
6. Cree una función que acepte un string con palabras separadas por un guión 
    y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''
def countMayusAndNoMayus(text):
    mayus =  []
    noMayus = []
    for char in text:
        if char.isupper():
            mayus.append(char)
        elif char.islower():
            noMayus.append(char)
    print(f'There’s {len(mayus)} upper cases and {len(noMayus)} lower cases')

countMayusAndNoMayus('I love Nación Sushi')

def sortString(text):
    listOfWords = sorted(text.split('-'))
    return '-'.join(listOfWords)

print(sortString('python-variable-funcion-computadora-monitor'))

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

