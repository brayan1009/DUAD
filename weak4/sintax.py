'''
💪🏽 **Ejercicios**
1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
    *Los errores son oportunidades de aprendizaje.*
    2. Por ejemplo:
        1. string + string → ?
        2. string + int → ?
        3. int + string → ?
        4. list + list → ?
        5. string + list → ?
        6. float + int → ?
        7. bool + bool → ?
2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

3. Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

4. Cree un programa que le pida tres números al usuario y muestre el mayor.
5. Dada `n` cantidad de grades de un estudiante, calcular:
    1. Cuantas grades tiene aprobadas (mayor a 70).
    2. Cuantas grades tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.

'''
import random

print("Bienvenido al Sistema de Operaciones")
print("Por Favor seleccione del catalogo de opciones la que quiera aplicar. Para salir , precione -1.")
currentOption = 0

def showOptions():
    print('''
    1- Conocer mi estado de vida(bebe, adolocente, etc)
    2- Adivina el numero secreto
    3- Administracion de grades
    4- Mayor numero de 3
    ''')

def runLifeCycleDefiner():
    name = input("Ingrese su nombre: ")
    lastName = input("Ingrese su apellido: ")
    age = int(input("Ingrese su edad: "))
    
    currentLifeCycleState = ''
    
    if age < 4:
        currentLifeCycleState = "Bebe"
    elif 4 <= age < 12:
        currentLifeCycleState = "Niño"
    elif 12 <= age < 18:
        currentLifeCycleState = "Adolescente"
    elif 18 <= age < 32:
        currentLifeCycleState = "Adulto Joven"
    elif 32 <= age < 60:
        currentLifeCycleState = "Adulto"
    elif age >= 60:
        currentLifeCycleState = "Adulto Mayor"
    
    print(f"{name} {lastName} tiene {age} años y es {currentLifeCycleState}")

def guessMagicNumber():
    magicNumber = random.randint(1,10)
    userNumber = 0
    while userNumber != magicNumber:

        userNumber = int(input('Ingrese un numero: '))

        if userNumber != magicNumber:
            print("Lo siento! Intenta de nuevo")

    print("Felicidades! Adivinaste")

def highestNumber():

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    num3 = float(input("Ingrese el tercer numero: "))

    mayor = max(num1, num2, num3)

    print(f"El numero mayor es: {mayor}")

def gradesProcessor():

    gradesNumber = int(input("Ingrese la cantidad de grades: "))
    grades = []

    for i in range(gradesNumber):
        grade = float(input(f"Ingrese la nota {i+1}: "))
        grades.append(grade)

    passing = [g for g in grades if g >= 70]
    failing = [g for g in grades if g < 70]

    countPassing = len(passing)
    countFailing = len(failing)

    avgTotal = sum(grades) / gradesNumber if gradesNumber > 0 else 0
    avgPassing = sum(passing) / countPassing if countPassing > 0 else 0
    avgFailing = sum(failing) / countFailing if countFailing > 0 else 0

    # Mostrar resultados
    print(f"Cantidad de notas aprobadas: {countPassing}")
    print(f"Cantidad de notas desaprobadas: {countFailing}")
    print(f"Promedio de todas las notas: {avgTotal:.2f}")
    print(f"Promedio de notas aprobadas: {avgPassing:.2f}")
    print(f"Promedio de notas desaprobadas: {avgFailing:.2f}")
      


while currentOption != -1:
    showOptions()
    userOption = input("Ingrese un digito: ")
    currentOption = int(userOption)
    if currentOption not in [-1,1,2,3,4]:
        print("Ingrese una opcion valida")

    if currentOption == 1:
        runLifeCycleDefiner()
    elif currentOption == 2:
        guessMagicNumber()
    elif currentOption == 3:
        gradesProcessor()
    elif currentOption == 4:
        highestNumber()
    elif currentOption == -1:
        print("Gracias por usar el sistema. Hasta luego!! ")



