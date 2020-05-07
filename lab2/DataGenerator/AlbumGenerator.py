from BaseGenerator import BaseGenerator
from enum import Enum
import random


class AlbumType(Enum):
    album = 'album'
    compilation = 'compilation'
    concert = 'concert'

    @classmethod
    def get_type(cls):
        return random.choice([AlbumType.album.value, AlbumType.compilation.value, AlbumType.concert.value])


class AlbumGenerator(BaseGenerator):

    def get_params(self):
        album = {
            'name': self.person.last_name(),
            'year': self.generic.datetime.year(),
            'duration': self.generic.datetime.time(),
            'quantity': self.generic.numbers.integer_number(start=0, end=100),
            'icon_path': self.generic.path.project_dir(),
            'type': AlbumType.get_type()
        }
        return album

    def get_primary_key_data(self, num):
        return range(0, num - 1)
