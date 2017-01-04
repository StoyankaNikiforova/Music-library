import os
import re
from song_class import Song
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from playlist_class import Playlist


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def get_music_files(self):
        music_files = [f for f in os.listdir(self.path) if (f.endswith('.mp3') or f.endswith('.ogg'))]
        return music_files

    def generate_palylist(self):
        folder_name = (re.findall('\w+', self.path)).pop()
        playlist = Playlist(folder_name, True, True)

        files = self.get_music_files()
        for f in files:
            print(f)
            tags = ID3('{}/{}'.format(self.path, f))
            print(tags.pprint())
            song = Song()
            playlist.songs.append(song)

        return playlist
