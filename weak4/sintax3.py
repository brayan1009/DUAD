'''
3. Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

'''
import random



def guessMagicNumber():
    magicNumber = random.randint(1,10)
    userNumber = 0
    while userNumber != magicNumber:

        userNumber = int(input('Ingrese un numero: '))

        if userNumber != magicNumber:
            print("Lo siento! Intenta de nuevo")

    print("Felicidades! Adivinaste")


guessMagicNumber()



