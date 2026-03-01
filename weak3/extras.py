"""
Ejercicios Extra
Cree un algoritmo que use print() para mostrar su nombre completo, su edad, su color favorito y su comida preferida. Debe presentar cada dato en una línea distinta
Ejemplo:
Salida:
"Mi nombre es Jean Carlo"
"Yo tengo 27 años"
"Mi color favorito es el Azul"
"Mi comida favorita es la Sopa de marisco"
​
Cree un algoritmo que muestre cuántos años tendrá usted dentro de 10 años. El algoritmo debe usar print() y una operación de suma
Ejemplo:
Salida:
"Dentro de 10 años yo tendré 37 años" 
​
Cree un algoritmo que defina una cantidad de metros (por ejemplo, 5) y luego use print() para mostrar cuántos centímetros son
Ejemplo:
Salida:
"5 metros son 500 centímetros"
"""
name = "Brayan"
age = 30

favColor = "Black"
favFood = "Pizza"
print(f"""My name is {name}, I'm {age} years old. Nice to meet you.
        My Favorite color is {favColor} 
        My favorite food is {favFood}""")


print(f"My age in ten years will be {age+10}")

meters = 10
print(f"{meters} m converted to centimeters is equal to {meters*100} cm")