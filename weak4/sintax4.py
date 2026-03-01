'''
4. Cree un programa que le pida tres números al usuario y muestre el mayor.
'''

def highestNumber():

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    num3 = float(input("Ingrese el tercer numero: "))

    mayor = max(num1, num2, num3)

    print(f"El numero mayor es: {mayor}")

highestNumber()



