import csv
'''
1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB
    2. Ejemplo de archivo final:
        
        ```
        nombre,genero,desarrollador,clasificacion
        Grand Theft Auto IV,Accion,Rockstar Games,M
        The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
        Tony Hawk's Pro Skater 2,Deportes,Activision,T
        ```

'''

file_headers = (
    'Name', 
    'genre', 
    'Developer', 
    'Rating'
)

def get_game_data():
    game_list = []
    while True:
        try:
            number_of_games = int(input('How many video games do you want to add? '))
            if number_of_games <= 0:
                print('Please enter a positive integer.')
                continue
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    try:
        for _game in range(number_of_games):
            print(f'Entering data for game {_game + 1}:')
            name = input('Type game name: ')
            genre = input('Type game genre: ')
            developer = input('Type game developer: ')
            rating = input('Type game ESRB rating: ')
            game_list.append({
                'Name': name,
                'genre': genre,
                'Developer': developer,
                'Rating': rating
            })
        return game_list
    except ValueError as error:
        print(f'Error trying to convert input')


def write_video_games_to_csv(file_path):
    games_to_add = get_game_data()
    try:
        with open(file_path, mode='w',encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=file_headers)
            writer.writeheader()
            for game in games_to_add:
                writer.writerow(game)
        print(f'Games written to {file_path} successfully.')
    except FileNotFoundError as error:
        print(f'File was not found: {error}')
'''
2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
    1. Ejemplo de archivo final:
        
        ```
        nombre	genero	desarrollador	clasificacion
        Grand Theft Auto IV	Accion	Rockstar Games	M
        The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
        Tony Hawk's Pro Skater 2	Deportes	Activision	T
        ```

'''

def write_video_games_to_csv_v2(file_path):
    games_to_add = get_game_data()
    try:
        with open(file_path, mode='w',encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=file_headers, dialect='excel-tab')
            writer.writeheader()
            writer.writerows(games_to_add)
        print(f'Games written to {file_path} successfully.')
    except FileNotFoundError as error:
        print(f'File was not found: {error}')



'''
Running the functions
'''
write_video_games_to_csv('files/video_games.csv')
write_video_games_to_csv_v2('files/video_games_tab.csv')