'''
Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
Lea sobre el resto de métodos de la clase File de Python aquí y cree una tabla donde explique qué hace cada uno. No necesita usar código para esto, es solo crear una tabla en Notion o Word.
Siga el siguiente formato:
Método
Descripción
read()
Lee y retorna todo el contenido del archivo
readlines()
Lee todo el contenido del archivo y retorna una lista con cada línea.
write()
Escribe contenidos en un archivo.
'''
def read_songs(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            songs = file.readlines()
            sorted_songs = sorted([song.strip() for song in songs])
            print(f"Songs reading from file: {sorted_songs}")
    except FileNotFoundError:
        print("File not found.")
        return []
    
    write_songs('files/sorted_songs.txt', sorted_songs)

def write_songs(file_path, songs):
    try:
        with open(file_path, 'w',encoding='utf-8') as file:
            for song in songs:
                file.write(f"{song}\n")
        print(f"Songs wrote into the file: {songs}")
    except Exception as error:
        print(f"Can not write in this file: {error}")

read_songs('files/songs.txt')
