'''
2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
    usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
'''
import pprint


def dictionaryBasedOnLists():
    keys = ["nombre", "edad", "ciudad", "profesion", "salario"]
    values = ["Ana", 28, "Madrid", "Diseñadora", 3500]
    identity = dict(zip(keys,values))
    pprint.pprint(identity)


dictionaryBasedOnLists()
