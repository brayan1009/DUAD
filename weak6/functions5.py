'''
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
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

