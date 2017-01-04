import unittest
import json
from song_class import Song
from playlist_class import Playlist


class playlistTest(unittest.TestCase):
    def setUp(self):
        self.pl = Playlist("My_list", repeat=True, shuffle=True)
        self.pl.add_song(Song("Odin1", "Manomar", "The sons of Odin_01", "2:44"))
        self.pl.add_song(Song("Odin2", "Manomar", "The sons of Odin_02", "2:44"))
        self.pl.add_song(Song("Odin3", "Manomar", "The sons of Odin_03", "2:44"))
        self.pl.add_song(Song("Odin4", "Manomar", "The sons of Odin_04", "2:44"))

    def test_total_lenght(self):
        self.assertEqual(self.pl.total_lenght(), '00:10:56')

    def test_add_songs(self):
        songs = [Song("Odin1", "Mar", "The sons of Odin_01", "2:78"),
                 Song("Odin2", "Manomar", "The", "1:2:44"),
                 Song("Odin3", "Manomar", "The sons ", "2:44"),
                 Song("Odin90", "Manomar", "Theof Odi n_04", "2:44")]

        self.pl.add_songs(songs)
        self.pl.pprint_playlist()

    def test_artists(self):
        self.assertEqual(self.pl.artists(), "ghujoi,biiuo,  joipp, hiii")

    def test_pprint_playlist(self):
        self.pl.pprint_playlist()

    def test_save(self):
        self.assertTrue(self.pl.save())   


if __name__ == '__main__':
    unittest.main()
