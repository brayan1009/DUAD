'''
5. Dada `n` cantidad de grades de un estudiante, calcular:
    1. Cuantas grades tiene aprobadas (mayor a 70).
    2. Cuantas grades tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
'''

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
      
gradesProcessor()

