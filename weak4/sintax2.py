'''
2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
'''

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

runLifeCycleDefiner()
      



