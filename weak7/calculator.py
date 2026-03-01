'''
Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar,
multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa 
un número invalido a la hora de hacer la operación.
'''
RED = '\033[91m'
GREEN = '\033[92m'
END_COLOR = '\033[0m'
def show_options():
    print('''
    1- Suma
    2- Resta
    3- Multiplicacion
    4- Division
    5- Borrar resultado
    6- Mostrar acumulado
    ''')

def sum_numbers(base_number, num_to_apply):
    try:
        return base_number + num_to_apply
    except Exception as error:
        print(f"{RED}Error encontrado al sumar: {error}{END_COLOR}")


def subtract_numbers(base_number, num_to_apply):
    try:
        return base_number - num_to_apply
    except Exception as error:
        print(f"{RED}Error encontrado al restar: {error}{END_COLOR}")


def multiply_numbers(base_number, num_to_apply):
    try:
        return base_number * num_to_apply
    except Exception as error:
        print(f"{RED}Error encontrado al multiplicar: {error}{END_COLOR}")


def divide_numbers(base_number, num_to_apply):
    try:
        return base_number / num_to_apply
    except ZeroDivisionError:
        print(f"{RED}No puedes dividir por cero{END_COLOR}")
    except Exception as error:
        print(f"{RED}Error encontrado al dividir: {error}{END_COLOR}")


def operation_handler(option, base_number):

    if option == 5:
        print(f"{GREEN}Resultado borrado. Numero actual es 0.0{END_COLOR}")
        return 0.0

    try:
        num_to_apply = float(input("Digite el segundo numero para aplicar la operacion: "))
        operations_dictionary = {
            1: sum_numbers,
            2: subtract_numbers,
            3: multiply_numbers,
            4: divide_numbers,
        }
        operation = operations_dictionary.get(option)
        if operation is None:
            print(f"{RED}Opcion de operacion invalida{END_COLOR}")
            return None
        return operation(base_number, num_to_apply)
    except ValueError as error:
        print(f"{RED}Debe digitar unicamente numeros: {error}{END_COLOR}")

operation_chosen = 0
try:
    user_option = float(input("Ingrese un numero base para empezar a operar sobre el : "))
except ValueError:
    print(f"{RED}Entrada invalida. Se usara 0.0 como valor inicial{END_COLOR}")
    user_option = 0.0

while True:
    show_options()
    try:
        operation_chosen = int(input("Ingrese el numero de operacion a realizar: "))
    except ValueError:
        print(f"{RED}Opcion invalida: debe digitar un numero{END_COLOR}")
        continue

    if operation_chosen == -1:
        print("Gracias por usar el sistema. Hasta luego!! ")
        break

    if operation_chosen == 6:
        print(f"Resultado acumulado actual: {user_option}")
        continue

    operation_result = operation_handler(operation_chosen, user_option)

    if operation_result is not None:
        print(f"{GREEN}El resultado de la operacion es: {operation_result}{END_COLOR}")
        user_option = operation_result
    else:
        print(f"{RED}No se pudo realizar la operacion, opcion no valida o error en entrada{END_COLOR}")
        continue
