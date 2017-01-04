import unittest
from music_crawler import MusicCrawler


class TestMusicCrawler(unittest.TestCase):
    def setUp(self):
        self.mcw = MusicCrawler('/home/tanija/Music/Ruski')

    def test_get_music_files(self):
        self.assertSequenceEqual(self.mcw.get_music_files(), [efwef, feje.mp3, cdk])
        
    def test_generate_palylist(self):
        self.assertEqual(self.mcw.generate_palylist(), {})


if __name__ == '__main__':
    unittest.main()
