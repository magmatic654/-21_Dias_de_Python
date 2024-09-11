# En este ejercicio, se solicita implementar una playlist utilizando un stack en Python.

# Se debe crear la clase Playlist con las siguientes propiedades: top, bottom y length, para representar el tope, la base y la longitud de la pila, respectivamente.

# La clase Playlist debe tener los siguientes métodos:

# addSong(song): Este método permite agregar una canción a la pila. La canción se agrega en el tope de la pila.

# playSong(): Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla. Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista".

# getPlaylist(): Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de reproducción, desde la última agregada hasta la primera.

# Ejemplo 1:

# Input:
# playlist = Playlist()
# playlist.addSong("Bohemian Rhapsody") 
# playlist.addSong("Stairway to Heaven") 
# playlist.addSong("Hotel California")

# Output: 
# print(playlist.playSong()) # Output: "Hotel California" 
# print(playlist.playSong()) # Output: "Stairway to Heaven" 
# print(playlist.playSong()) # Output: "Bohemian Rhapsody" 
# print(playlist.playSong()) # Output: Error: No hay canciones en la lista 

# Ejemplo 2:

# Input:
# playlist = Playlist()
# playlist.addSong("Bohemian Rhapsody")
# playlist.addSong("Stairway to Heaven")
# playlist.addSong("Hotel California")
# print(playlist.getPlaylist()) 

# Output: ["Hotel California", "Stairway to Heaven", "Bohemian Rhapsody"]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Playlist:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def addSong(self, song):
        new_song = Node(song)  
        if self.length == 0:
            self.bottom = new_song
            self.top = new_song
        else:
            new_song.next = self.top
            self.top = new_song
        self.length += 1
    
    def popSong(self):
        if self.length == 0:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped_Song = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_Song.value
    
    def playSong(self):
        if self.length == 0:
            raise Exception('No hay canciones en la lista')
        return self.popSong()

    def getPlaylist(self):
        songs_array = []
        current_song = self.top
        while current_song :
            print(current_song.value)
            songs_array.append(current_song.value)
            current_song = current_song.next
        return songs_array
    

playlist = Playlist()
playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")
print(playlist.getPlaylist()) 