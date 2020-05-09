from BaseGenerator import BaseGenerator
import random
from Utils import open_connection, close_connection


class SongGenerator(BaseGenerator):
    cursor, conn = open_connection()
    cursor.execute('SELECT id FROM album;')
    id_albums = cursor.fetchall()
    close_connection(cursor, conn)

    def get_primary_key_data(self, num):
        return range(0, num - 1)

    def get_params(self):
        song = {
            'name': self.person.first_name(),
            'year': self.generic.datetime.year(),
            'path': self.generic.path.project_dir(),
        }

        if bool(random.getrandbits(1)):
            if bool(self.id_albums) is True:
                song.update({'album': random.choice(self.id_albums)})
        else:
            song.update({'album': None})
            print(song)
        return song
