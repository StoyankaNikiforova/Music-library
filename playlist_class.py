import json
from random import randint
import glob
from prettytable import PrettyTable


class Playlist:
    def __init__(self, name="Code", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def add_songs(self, songs):
        self.songs += songs
        return "Ueaa!"


    def total_lenght(self):
        lengh = 0
        for s in self.songs:
            lengh += s.lenght(seconds=True)
        hours = int(lengh//3600)
        minutes = int((lengh % 3600) / 60)
        seconds = int((lengh % 3600) % 60)

        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    def artists(self):
        artists = {}
        for song in self.songs:
            if song.artist in artists:
                artists[song.artist] += 1
            else:
                artists[song.artist] = 1
        return artists

    def next_song(self, current_song):
        current_index = self.songs.index(current_song)
        next_index = current_index + 1
        last_index = len(self.songs)-1

        if self.shuffle:
            next_index = randint(0, last_index)

        if self.repeat and next_index == last_index:
            next_index = 0

        return self.songs[next_index]

    def pprint_playlist(self):
        table = PrettyTable(["Artist", "Song", "Lenght"])
        for song in self.songs:
            table.add_row([song.artist, song.title, song.lenght_input])

        print(table)

    def save(self):
            json_data = {}
            json_data['name'] = self.name
            json_data['songs'] = []

            playlist = [[song.title, song.artist, song.album, song.lenght_input]
                        for song in self.songs]

            for song in playlist:
                json_data['songs'].append({'title': song[0], 'artist': song[1],
                                          'album': song[2], 'length': song[3]})

            with open('' + self.name + '.json', 'w') as output:
                json.dump(json_data, output, indent=True)

    @staticmethod
    def load(filename):
        songs = []

        with open(filename, 'r') as f:
            content = f.read()
            data = json.loads(content)
            playlist = Playlist(data['name'], repeat=True)

            for song in data['songs']:
                songs.append(Song(song['title'], song['artist'],
                                  song['album'], song['length']))

            playlist.add_songs(songs)

            return playlist
