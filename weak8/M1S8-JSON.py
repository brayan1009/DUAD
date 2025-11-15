import json

def add_new_pokemon():
    while True:
        try:
            name = input("Enter Pokémon name: ")
            pokemon_type = input("Enter Pokémon type: ")
            hp = int(input("Enter HP stat: "))
            attack = int(input("Enter Attack stat: "))
            defense = int(input("Enter Defense stat: "))
            special_attack = int(input("Enter Special Attack stat: "))
            special_defense = int(input("Enter Special Defense stat: "))
            speed = int(input("Enter Speed stat: "))
            break
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
      
    return {
            "name": {
                "english": name
            },
            "type": [
                pokemon_type
            ],
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": special_attack,
                "Sp. Defense": special_defense,
                "Speed": speed
            }
        }


def read_pokemons(file_path):
    pokemons = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemons = json.load(file)
            print(f"Pokémons reading from file: {pokemons}")
    except FileNotFoundError:
        print("File not found.")
        return []
    new_pokemon = add_new_pokemon()
    pokemons.append(new_pokemon)

    try:
        with open(file_path, 'w', encoding='utf-8') as write_file:
            json.dump(pokemons, write_file, indent=4) 
        print(f"Pokémon list updated successfully. Total: {len(pokemons)}")

    except IOError:
        print("Error writing to file.")
    
read_pokemons('files/pokemons.json')