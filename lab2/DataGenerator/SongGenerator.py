from BaseGenerator import BaseGenerator
import random
from Utils import open_connection, close_connection


class SongGenerator(BaseGenerator):
    cursor, conn = open_connection()
    cursor.execute('SELECT count(*) FROM album;')
    length = cursor.fetchone()[0]
    close_connection(cursor, conn)

    def get_primary_key_data(self, num):
        return range(0, num - 1)

    def get_params(self):
        song = {
            'name': self.person.first_name(),
            'path': self.generic.path.project_dir(),
        }

        print(self.length)
        if bool(random.getrandbits(1)):
            if self.length > 0:
                album_id = random.randint(0, self.length)
                song.update({'album': album_id[0]})
        else:
            song.update({'album': None})
            print(song)
        return song
