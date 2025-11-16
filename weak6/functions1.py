'''
1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
'''
def printOtherThing():
    print('other thing')

def printOneThing():
    print(f"Im just printing", end=" ")
    printOtherThing()

printOneThing()
