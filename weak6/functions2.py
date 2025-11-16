'''
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
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
