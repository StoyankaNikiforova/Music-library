import unittest
from song_class import Song


class testSong(unittest.TestCase):
    def setUp(self):
        self.s = Song('fj', 'xhch', 'drdy', '4:09')
        self.s2 = Song('fj', 'xhch', 'drdy', '1:04:09')
        self.s3 = Song('fj', 'xhch', 'drdy', '2:25:09')

    def test_lenght(self):
        self.assertEqual(self.s.lenght(seconds=True), 249)

    def test_lenght2(self):
        self.assertEqual(self.s2.lenght(minutes=True), 64)

    def test_lenght3(self):
        self.assertEqual(self.s3.lenght(hours=True), 2)

    def test_lenght4(self):
        self.assertEqual(self.s.lenght(), '2')


if __name__ == '__main__':
    unittest.main()
