import re


class Song:
    def __init__(self, title, artist, album, lenght):
        self.title = title
        self.artist = artist
        self.album = album
        self.lenght_input = lenght

    def __str__(self):
        return "{0} - {1} from {2} - {3}".format(self.artist, self.title,
                                                 self.album, self.lenght_input)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return (hash(self.title) ^ hash(self.lenght_input)) + 76

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.lenght_input == other.lenght_input

    def lenght(self, seconds=False, minutes=False, hours=False):
        len_atr = re.findall('\d+', self.lenght_input)
        imp_sec = int(len_atr.pop())
        imp_mins = int(len_atr.pop())
        imp_hours = 0
        if len(len_atr) == 1:
            imp_hours = int(len_atr.pop())

        if seconds:
            ss = imp_sec + imp_mins * 60 + imp_hours * 3600
            return ss
        if minutes:
            ms = imp_mins + imp_hours * 60
            return ms
        if hours:
            return imp_hours
        return self.lenght_input
